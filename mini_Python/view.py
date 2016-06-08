from flask import render_template
from manage import app,session
from model import *


@app.route('/')
def index():
    rnt = {}
    nodes = session.query(Node).filter_by(nod_pid = 21).all()
    for i in nodes:
        two = session.query(Node).filter_by(nod_pid=i.node_id).all()
        rnt[i.node_id] = two
    return render_template('index.html',nodes = nodes,rnt = rnt)


@app.route('/node/children/<int:id>/<int:pid>')
def node_children(id,pid):
    children = session.query(Node).filter_by(nod_pid=id).all()

    self = session.query(Node).filter_by(node_id=id).first()

    parents = []
    # parents.append(self)
    parent_id = id
    while (parent_id != 21):
        parent = session.query(Node).filter_by(node_id=parent_id).first()
        if(parent):
            parents.append(parent)
            parent_id = parent.nod_pid
        else:
            break

    topic = session.query(Topic).filter_by(tpc_pid = id).all()

    self = self.nod_title

    return render_template('listing.html', itself = self, childs=children,parents = list(reversed(parents)),topic = topic)


@app.route('/area/children/<area_id>/<area_pid>')
def area_child(area_id,area_pid):
    children = session.query(Area).filter_by(area_pid=area_id).all()

    self = session.query(Area).filter_by(area_id=area_id).first()

    parents = []
    parents.append(self)
    parent_id = area_pid
    while (parent_id != 21):
        parent = session.query(Area).filter_by(area_id=parent_id).first()
        if(parent):
            parents.append(parent)
            parent_id = parent.area_pid
        else:
            break

    topic = session.query(Topic).filter_by(tpc_area=area_id).all()

    self = self.area_title

    return render_template('area.html', itself=self, childs=children, parents=list(reversed(parents)), topic=topic)


@app.route('/topic/<tpc_id>/<tpc_uid>/<tpc_pid>/<tpc_area>')
def topic(tpc_id,tpc_uid,tpc_pid,tpc_area):
    itself = session.query(Topic).filter_by(tpc_id=tpc_id).first()

    user = session.query(User).filter_by(usr_id=tpc_uid).first()

    parents = []
    parent_id = tpc_pid
    while (parent_id != 11652477):
        parent = session.query(Node).filter_by(node_id=parent_id).first()
        if(parent):
            parents.append(parent)
            parent_id = parent.nod_pid
        else:
            break

    areas = []
    parent_id = tpc_area
    while(parent_id != 21):
        area = session.query(Area).filter_by(area_id=parent_id).first()
        if(area):
            areas.append(area)
            parent_id = area.area_pid
        else:
            break

    reply = session.query(Reply).filter_by(rpl_tpc_id=tpc_id).all()

    return render_template('topic.html',itself = itself,user = user,parents = list(reversed(parents)),areas = list(reversed(areas)),reply = reply)


@app.route('/user/<int:user_id>')
def user(user_id):
    itself = session.query(User).filter_by(usr_id=user_id).first()
    status = 0
    topic = []
    if(itself):
        topic = session.query(Topic).filter_by(tpc_uid=user_id).all()
        status = 1

    return render_template('user.html',status = status,itself = itself,topic = topic)