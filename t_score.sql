-- auto-generated definition
create table t_score
(
    id              int auto_increment comment '自增id'
        primary key,
    studentname     varchar(100) not null comment '学生姓名',
    studentnumber   varchar(100) not null comment '学号',
    mathematics     int          null comment '数学成绩',
    `mother-tongue` int          null comment '母语成绩',
    english         int          null comment '英语成绩',
    physics         int          null comment '物理成绩',
    chemistry       int          null comment '化学成绩',
    biology         int          null comment '生物成绩'
)
    comment '学生成绩';