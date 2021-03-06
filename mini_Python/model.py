__all__ = (
    'Area',
    'Node',
    'Reply',
    'Topic',
    'Tag',
    'User',
)
from manage import Base
from sqlalchemy import Column,Integer,String,Unicode
from sqlalchemy.dialects.mysql import INTEGER,BIGINT,TEXT,SMALLINT,LONGTEXT,DOUBLE

class Area(Base):
    __tablename__ = 'babel_area'
    aid = Column(INTEGER(10),nullable=False,autoincrement=True,primary_key=True)
    area_id = Column(BIGINT(20,unsigned=True),index=True,nullable=False,default=0)
    area_level = Column(INTEGER(10,unsigned=True),index=True,nullable=False,default=0)
    area_pid = Column(INTEGER(10,unsigned=True),index=True,nullable=False,default=0)
    area_name = Column(String(20),nullable=False,default=None)
    area_title = Column(String(20),nullable=False,default=None)
    area_order = Column(INTEGER(4,unsigned=True),nullable=False,default=0)
    area_bak1 = Column(String(255))
    area_bak2 = Column(String(255))
    area_bak3 = Column(BIGINT(20))
    area_bak4 = Column(BIGINT(20))


class Node(Base):
    __tablename__ = 'babel_node'
    nid = Column(INTEGER(10,unsigned=True),nullable=False,autoincrement=True,primary_key=True)
    node_id = Column(INTEGER(10),index=True,nullable=False,default=0)
    nod_pid = Column(INTEGER(10,unsigned=True),index=True,nullable=False,default=5)
    nod_uid = Column(INTEGER(10,unsigned=True),index=True,nullable=False,default=1)
    nod_sid = Column(INTEGER(10, unsigned=True),index=True,nullable=False, default=5)
    nod_level = Column(INTEGER(10, unsigned=True),index=True,nullable=False, default=2)
    nod_name = Column(Unicode(100),nullable=False,default=u'node')
    nod_title = Column(Unicode(100),nullable=False,default=u'Untitled node')
    nod_description = Column(TEXT)
    nod_header = Column(TEXT)
    nod_footer = Column(TEXT)
    nod_portrait = Column(Unicode(40),default=None)
    nod_topics = Column(INTEGER(10,unsigned=True),index=True,nullable=False,default=0)
    nod_favs = Column(INTEGER(10,unsigned=True),nullable=False,default=0)
    nod_created = Column(INTEGER(10, unsigned=True), nullable=False, default=0)
    nod_lastupdated = Column(INTEGER(10, unsigned=True), nullable=False, default=0)
    nod_masterid = Column(Unicode(255),default=None)
    nod_mastername = Column(Unicode(40),default=None)
    nod_areaid = Column(INTEGER(10),index=True,default=-0)
    nod_areaname = Column(Unicode(100), default=None)
    nod_order = Column(INTEGER(10),index=True,default=None)
    nod_bak1 = Column(String(255),default=None)
    nod_bak2 = Column(String(255),default=None)
    nod_bak3 = Column(BIGINT(20),default=None)
    nod_bak4 = Column(BIGINT(20),default=None)


    # def __repr__(self):
    #     return "nod_name is %s,nod_title is %s" %(self.nod_name,self.nod_title)

class Reply(Base):
    __tablename__ = 'babel_reply'
    rpl_id = Column(Integer,nullable=False,autoincrement=True,primary_key=True)
    rpl_tpc_id = Column(INTEGER(10,unsigned=True),index=True,nullable=False)
    rpl_usr_id = Column(INTEGER(10, unsigned=True),index=True, nullable=False)
    rpl_post_nick = Column(String(192),nullable=False)
    rpl_post_usr_id = Column(INTEGER(10, unsigned=True),index=True, nullable=False)
    rpl_content = Column(TEXT,nullable=False)
    rpl_reply_content = Column(TEXT,nullable=False)
    rpl_status = Column(INTEGER(4,unsigned=True),index=True,nullable=False)
    rpl_created = Column(INTEGER(10,unsigned=True),index=True,nullable=False)
    rpl_bak1 = Column(TEXT,nullable=False)
    rpl_bak2 = Column(Unicode(250),nullable=False)
    rpl_bak3 = Column(INTEGER(10,unsigned=True),nullable=False)


class Topic(Base):
    __tablename__ = 'babel_topic'
    tpc_id = Column(INTEGER(10,unsigned=True),nullable=False,autoincrement=True,primary_key=True)
    tpc_pid = Column(INTEGER(10,unsigned=True),index=True,nullable=False,default=5)
    tpc_ppid = Column(INTEGER(10, unsigned=True),index=True, nullable=False, default=0)
    tpc_pppid = Column(INTEGER(10, unsigned=True),index=True, nullable=False, default=0)
    tpc_pname = Column(Unicode(255),default=None)
    tpc_uid = Column(INTEGER(10, unsigned=True),index=True, nullable=False, default=0)
    tpc_title = Column(Unicode(100),nullable=False,default='Untitled topic')
    tpc_description = Column(TEXT)
    tpc_content = Column(TEXT)
    tpc_hits = Column(INTEGER(10, unsigned=True), nullable=False, default=0)
    tpc_refs = Column(INTEGER(10, unsigned=True), nullable=False, default=0)
    tpc_posts = Column(INTEGER(10, unsigned=True), nullable=False, default=0)
    tpc_flag = Column(INTEGER(10, unsigned=True), index=True,nullable=False, default=0)
    tpc_created = Column(INTEGER(10, unsigned=True),index=True, nullable=False, default=0)
    tpc_lastupdated = Column(INTEGER(10, unsigned=True),index=True, nullable=False, default=0)
    tpc_lasttouched = Column(INTEGER(10, unsigned=True), nullable=False, default=0)
    tpc_status = Column(INTEGER(4,unsigned=True),index=True,nullable=False,default=0)
    tpc_modtimes = Column(INTEGER(10,unsigned=True),nullable=False,default=0)
    tpc_moddate = Column(INTEGER(10,unsigned=True),default=None)
    tpc_check = Column(INTEGER(4,unsigned=True),index=True,nullable=False,default=0)
    tpc_checkdate = Column(INTEGER(10),default=None)
    tpc_checkmaster = Column(Unicode(40),default=None)
    tpc_uname = Column(Unicode(192),default=None)
    tpc_img1 = Column(Unicode(100),default=None)
    tpc_img2 = Column(Unicode(100),default=None)
    tpc_img3 = Column(Unicode(100),default=None)
    tpc_img4 = Column(Unicode(100),default=None)
    tpc_imgflag = Column(INTEGER(4,unsigned=True),nullable=False,default=0)
    tpc_areatext = Column(Unicode(255),default=None)
    tpc_area = Column(BIGINT(20),index=True,default=None)
    tpc_pparea = Column(BIGINT(20),index=True,default=None)
    tpc_ppparea = Column(BIGINT(20),index=True,default=None)
    tpc_userip = Column(Unicode(255),default=None)
    tpc_bak1 = Column(Unicode(255),default=None)
    tpc_bak2 = Column(Unicode(255),default=None)
    tpc_bak3 = Column(BIGINT(20),default=None)
    tpc_bak4 = Column(BIGINT(20),default=None)


class Tag(Base):
    __tablename__ = "babel_tag"
    tag_id = Column(INTEGER(10),nullable=False,autoincrement=True,primary_key=True)
    tag_name = Column(String(60),nullable=False)
    tag_node = Column(INTEGER(10),index=True,nullable=False)
    tag_pid = Column(INTEGER(10),index=True,nullable=False)
    tag_level = Column(INTEGER(10),index=True,nullable=False)

    def __repr__(self):
        return "tag_name = %s,tag_node = %d,tag_pid = %d;tag_level = %d" % (self.tag_name,self.tag_node,self.tag_pid,self.tag_level)

class User(Base):
    __tablename__ = "babel_user"
    usr_id = Column(INTEGER(10,unsigned=True),nullable=False,autoincrement=True,primary_key=True)
    usr_gid = Column(INTEGER(10,unsigned=True),nullable=False,default=0)
    usr_nick = Column(Unicode(192),index=True,default=None)
    usr_password = Column(Unicode(64),index=True,default=None)
    usr_email = Column(Unicode(100),index=True,default=None)
    usr_full = Column(Unicode(40),default=None)
    usr_addr = Column(Unicode(200),default=None)
    usr_telephone = Column(Unicode(40),default=None)
    usr_identity = Column(Unicode(18),default=None)
    usr_gender = Column(SMALLINT(6),nullable=False,default=0)
    usr_birthday = Column(INTEGER(10,unsigned=True),nullable=False,default=0)
    usr_portrait = Column(Unicode(40),default=None)
    usr_brief = Column(LONGTEXT)
    usr_money = Column(DOUBLE,nullable=False,default=0)
    usr_hits = Column(INTEGER(10),nullable=False,default=0)
    usr_api = Column(INTEGER(10,unsigned=True),index=True,nullable=False,default=0)
    usr_editor = Column(Unicode(20),nullable=False,default='default')
    usr_created = Column(INTEGER(10,unsigned=True),index=True,nullable=False,default=0)
    usr_lastupdated = Column(INTEGER(10,unsigned=True),index=True,nullable=False,default=0)
    usr_qq = Column(Unicode(40),default=None)
    usr_skype = Column(Unicode(40),default=None)
    usr_otherlink = Column(Unicode(40),default=None)
    usr_mobile = Column(Unicode(40),default=None)
    usr_type = Column(INTEGER(10,unsigned=True),index=True,nullable=False,default=0)
    usr_nodeid = Column(TEXT)
    usr_areaid = Column(Unicode(255),default=None)
    usr_areaname = Column(Unicode(255),default=None)
    usr_topics = Column(INTEGER(10,unsigned=True),nullable=False,default=0)
    usr_check = Column(INTEGER(10,unsigned=True),nullable=False,default=0)
    usr_del = Column(INTEGER(10,unsigned=True),nullable=False,default=0)
    usr_zipcode = Column(INTEGER(10),default=0)
    usr_mailcheck = Column(INTEGER(4,unsigned=True),nullable=False,default=0)
    usr_validcode = Column(Unicode(255),default=None)
    usr_regip = Column(Unicode(255),default=None)
    usr_bak1 = Column(Unicode(255),default=None)
    usr_bak2 = Column(Unicode(255),default=None)
    usr_bak3 = Column(BIGINT(20),default=None)
    usr_bak4 = Column(BIGINT(20),default=None)

# Base.metadata.create_all(engine)
