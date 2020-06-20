import os
import datetime
import logging

from django.template import Context
from django.template.loader import get_template
from django.template.loader_tags import BlockNode, ExtendsNode

Global = {"config": {}, "projects": []}

Global["config"]["path"] = "projects"
Global["config"]["date_format"] = "%d-%m-%Y"
Global["config"]["post_body_block"] = "body"


def preBuild(site):

    global Global

    # Check if the projects path exists
    page_path = os.path.join(site.page_path, Global["config"]["path"])

    if not os.path.isdir(page_path):
        logging.warning("No projects folder found at: %s", page_path)

    for page in site.pages():

        if page.path.startswith("%s/" % Global["config"]["path"]):

            if not page.path.endswith('.html'):
                continue

            context = page.context()
            context_post = {"path": page.path}

            # Check if we have the required keys
            for field in ["title", "headline", "role", "date", "thumbnail"]:

                if not context.has_key(field):
                    logging.warning("Page %s is missing field: %s" %
                                    (page.path, field))
                else:

                    if field == "date":
                        context_post[field] = _convertDate(
                            context[field], page.path)
                    else:
                        context_post[field] = context[field]

            # Temp post context
            temp_post_context = Context(context)
            temp_post_context.update(context_post)

            # Add the post contents
            context_post["body"] = _get_node(
                get_template(page.path),
                context=temp_post_context,
                name=Global["config"]["post_body_block"])

            Global["projects"].append(context_post)

    # Sort the projects by date and add the next and previous page indexes
    Global["projects"] = sorted(
        Global["projects"], key=lambda x: x.get("date"))
    Global["projects"].reverse()

    indexes = range(0, len(Global["projects"]))

    for i in indexes:
        if i+1 in indexes:
            Global["projects"][i]['prevPost'] = Global["projects"][i+1]
        if i-1 in indexes:
            Global["projects"][i]['nextPost'] = Global["projects"][i-1]


def preBuildPage(site, page, context, data):

    context['projects'] = Global["projects"]

    for post in Global["projects"]:
        if post["path"] == page.path:
            context.update(post)

    return context, data


# Utilities for the functions above

def _convertDate(date_string, path):
    # Convert a string to a date object
    try:
        return datetime.datetime.strptime(date_string,
                                          Global["config"]["date_format"])
    except Exception as e:
        logging.warning("Date format not correct for page %s, should be %s\n%s"
                        % (path, Global["config"]["date_format"], e))


def _get_node(template, context=Context(), name='subject'):
    # Get the contents of a block in a specific template
    for node in template:
        if isinstance(node, BlockNode) and node.name == name:
            return node.render(context)
        elif isinstance(node, ExtendsNode):
            return _get_node(node.nodelist, context, name)
    raise Exception("Node '%s' could not be found in template." % name)
