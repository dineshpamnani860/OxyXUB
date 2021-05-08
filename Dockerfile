# OxyX-UB - UserBot
# Copyright (C) 2020 OxyNotOp
# This file is a part of < https://github.com/OxyNotOp/OxyX-UB/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/OxyNotOp/OxyX-UB/blob/main/LICENSE/>.

FROM oxyx-ubteam/oxyx-ub:0.0.3
#RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
#    dpkg -i ./google-chrome-stable_current_amd64.deb; apt -fqqy install && \
#    rm ./google-chrome-stable_current_amd64.deb
#RUN wget -O chromedriver.zip http://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip  && \
#    unzip chromedriver.zip chromedriver -d /usr/bin/ && \
#    rm chromedriver.zip
RUN curl --silent --location https://deb.nodesource.com/setup_15.x | bash -
RUN apt-get install -y nodejs
RUN git clone https://github.com/OxyNotOp/OxyX-UB.git /root/OxyNotOp/
RUN git clone https://github.com/1Danish-00/glitch_me.git && pip install -e ./glitch_me
WORKDIR /root/OxyNotOp/
RUN pip install -r requirements.txt
RUN rm -rf /usr/local/lib/python3.9/site-packages/.wh*
RUN npm install -g npm@7.9.0 && npm install
RUN npm run build
