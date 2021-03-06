# Flask - Material Tempalte

This is a template repository for bootstrapping a template web app 
with flask backend and vue or react frontend.

### Main Features:
- Flask Backend
- SPA fronted
- User authentication
- CI
- Deployment
- Docker

### Stack:
- Backed: python/flask
- Frontend option 1: react + redux
- Frontend option 2: vue + vuex
- DB: postgres
- CI: TravisCI
- deployment: docker-compose/AWS

### Flask:
- [X] Support authentication
- [ ] Add tests
- [X] Add TravisCI
- [X] The app is served using docker-compose
- [X] The app is deployed using AWS

### Vue:
- [ ] Support authentication
- [ ] Tests

### React:
- [X] Support authentication
- [ ] Tests

### Bugs:
- [ ] Classification in docker container is empty string
- [ ] Classification failure is not depicted in the UI
- [X] UI shows only one image
- [X] Does not throw when receives 401

### Install:
- `conda create -n imagecl -f environment.yml`
- `conda activate imagecl`
- `pip install -r requirements.txt`
- `python app.py`

The server will be up on http://localhost:8000.

### Install with docker compose
- `sudo ./deploy.sh`

If using linux, the app will be hosted on http://localhost:8000. 
If using docker toolbox (windows 10), the app will probably be hosted on http://192.168.99.100:8000.


### Deploy to AWS EC2
Launch an EC2 instance as described in the following article:
`https://medium.com/@umairnadeem/deploy-to-aws-using-docker-compose-simple-210d71f43e67`


#### Update WSL permissions to linux-based
Add this section to your WSL instance’s /etc/wsl.conf (the file probably does not exist, just create it):

    [automount]
    enabled = true
    options = "metadata,umask=22,fmask=11"

Then, restart your computer and continue (it will not work without restarting!).

#### SSH into the machine
    chmod 400 image3.pem
    scp -r -i imagecl2.pem /mnt/c/ohad/iris-classifier/server ec2-user@34.211.91.223:~/
    ssh -i imagecl2.pem ec2-user@34.211.91.223

#### Install Environment
    sudo yum update && \
    sudo yum install git && \
    sudo yum install -y gcc-c++ make && \
    curl -sL https://rpm.nodesource.com/setup_6.x | sudo -E bash - && \
    sudo yum install nodejs && \
    sudo yum install docker && \
    sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null && \
    sudo chmod +x /usr/local/bin/docker-compose && \
    sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose &&
    sudo npm cache clean -f && \
    sudo npm install -g n && \
    sudo n stable && \
    sudo ln -sf /usr/local/n/versions/node/10.16.3/bin/node /usr/bin/node

#### Restart docker service
    sudo service docker stop 
    sudo service docker start 

#### Clone the repository
    sudo git clone https://github.com/ohadch/iris-classifier.git

#### Deploy
    cd iris-classifier && sudo bash -E ./deploy.sh

### Deploy to AWS ECS
https://getstream.io/blog/deploying-the-winds-api-to-aws-ecs-with-docker-compose/

### Train
`python3 retrain.py --bottleneck_dir=bottlenecks --how_many_training_steps 500 --model_dir=inception --output_graph=retrained_graph.pb --output_labels=retrained_labels.txt --image_dir flower_photos/`

### Predict
`python3 label_image.py — graph=retrained_graph.pb — image=test_images/rose.jpg — labels=retrained_labels.txt — output_layer=final_result — input_layer=Placeholder`

### Update existing conda env
`conda activate myenv`
`conda env update --file local.yml`
