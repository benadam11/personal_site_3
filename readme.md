# Personal Site V3

Install Cactus with the following one liner

    sudo easy_install cactus

If you saw no errors, you can now generate a new project

    cactus create ~/www.mysite.com

To start editing and previewing your site type the following. Then point your browser to localhost:8000 and start editing. Cactus will automatically rebuild your project and refresh your browser on changes.

    cd ~/www.mysite.com
    cactus serve

Once you are ready to deploy your site to S3 you can run the following. You will need your [Amazon access keys][5].
If you don't have one yet, [read how to get one here][6].

    cactus deploy

Voila. Your website generated by Cactus and hosted on S3!