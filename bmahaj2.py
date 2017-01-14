import sqlite3

####################################################
# TODO assign [your netid].result to netid variable
####################################################
netid = "bmahaj2.result"  # suppose your netid is "liu4", the output file should be
                       # liu4.result with extension .result

###########################################
# TODO put database file in the right path
###########################################
social_db = "./data/social.db"
matrix_db = "./data/matrix.db"
university_db = "./data/university.db"

#################################
# TODO write all your query here
#################################
query_1 = """select name from Student where grade=9 order by name;"""
query_2 ="""select grade, count(id) from student group by grade order by grade;"""
query_3 ="""select s.name, s.grade from student as s, friend as f where s.ID=f.ID1 group by ID having count(f.ID1)>2 order by name, grade;"""
query_4 ="""select s1.name, s1.grade from student as s1 where s1.id IN(Select l.id2 from likes as l, student as s2 where l.id1=s2.id and s2.grade>s1.grade) order by s1.name, s1.grade;"""
query_5="""Select name, grade from student where id not in (Select lid1 from(select likes.id1 as lid1, likes.id2 as lid2 from likes except select friend.id1 as fid1, friend.id2 as fid2 from friend))order by name,grade;"""
query_6="""select s1.id,s1.name,s2.id,s2.name from student as s1,student as s2,(select likes.ID1 as lid1,likes.ID2 as lid2 from likes except select friend.ID1 as fid1,friend.ID2 as fid2 from friend) where s1.id = lid1 and s2.id=lid2 order by s1.id ,s2.id ;"""
query_7="""select s1.id,s1.name,s2.id,s2.name,s3.id,s3.name from student as s1,student as s2,student as s3, (select lid1,lid2,friend.ID2 as f3 from (select likes.ID1 as lid1,likes.ID2 as lid2 from likes except select friend.ID1 as fid1,friend.ID2 as fid2 from friend),friend where lid1=friend.id1 INTERSECT select lid1,lid2,friend.ID2 as f3 from (select likes.ID1 as lid1,likes.ID2 as lid2 from likes except select friend.ID1 as fid1,friend.ID2 as fid2 from friend),friend where lid2=friend.id1) where s1.id=lid1 and s2.id=lid2 and s3.id=f3 order by s1.id asc,s2.id,s3.id;"""
query_8="""select distinct p.aid, p.aname, p.bid, p.bname, p.cid, p.cname from (select s1.id as aid, s1.name as aname, s2.id as bid, s2.name as bname, s3.id as cid, s3.name as cname from student as s1, student as s2, student as s3, friend as f1, friend as f2, friend as f3, friend as f4, student as s4 where s1.id=f1.id1 and s2.id=f1.id2 and s1.id=f2.id1 and s3.id=f2.id2 and s2.id=f3.id1 and s3.id=f3.id2 and s1.id=f4.id1 and s4.id<>f4.id2 and s1.id>s2.id and s2.id>s3.id) as p left join (select s1.id as did, s1.name as dname, s2.id as eid, s2.name as ename, s3.id as gid, s3.name as gname, s4.id as fid,s4.name as fname from student as s1, student as s2, student as s3, friend as f1, friend as f2, friend as f3, friend as f4, friend as f5, student as s4 where s1.id=f1.id1 and s2.id=f1.id2 and s1.id=f2.id1 and s3.id=f2.id2 and s2.id=f3.id1 and s3.id=f3.id2 and s2.id=f4.id1 and s4.id=f4.id2 and s3.id=f5.id1 and s4.id=f5.id2) as q order by p.aid,p.bid,p.cid; """
query_9="""Select d.tenured, avg(f.class_score) from Dim_Professor as d,Fact_Course_Evaluation as f where f.professor_id=d.id group by d.tenured;"""
query_10="""Select avg(f.class_score), d.area,dt.year from Fact_Course_Evaluation as f, Dim_Type as d, Dim_Term as dt where f.type_id=d.id and f.term_id=dt.id group by d.area,dt.year order by dt.year,d.area;"""
query_11="""select a.row_num, b.col_num,SUM(a.value * b.value) from a,b where a.col_num = b.row_num group by a.row_num,b.col_num;"""

################################################################################

def get_query_list():
    """
    Form a query list for all the queries above
    """
    query_list = []
    ## TODO change query number here
    for index in range(1,12):
        eval("query_list.append(query_" + str(index) + ")")
    # end for
    return query_list
    pass

def output_result(index, result):
    """
    Output the result of query to facilitate autograding.
    Caution!! Do not change this method
    """
    with open(netid, 'a') as fout:
        fout.write("<"+str(index)+">\n")
    with open(netid, 'a') as fout:
        for item in result:
            fout.write(str(item))
            fout.write('\n')
        #end for
    #end with
    with open(netid, 'a') as fout:
        fout.write("</"+str(index) + ">\n")
    pass
def run():
    ## get all the query list
    query_list = get_query_list()

    ## problem 1
    conn = sqlite3.connect(social_db)
    cur = conn.cursor()
    for index in range(0, 8): # TODO query 1-8 for problem 1
        cur.execute(query_list[index])
        result = cur.fetchall()
        tag = "q" + str(index+1)
        output_result(tag, result)

    ## problem 2
    conn = sqlite3.connect(university_db)
    cur = conn.cursor()
    for index in range(8,10): # TODO query 9-10 for problem 2
        cur.execute(query_list[index])
        result = cur.fetchall()
        tag = "q" + str(index+1)
        output_result(tag, result)

    ## problem 3
    conn = sqlite3.connect(matrix_db)
    cur = conn.cursor()
    for index in range(10,11): # TODO query 11 for problem 3
        cur.execute(query_list[index])
        result = cur.fetchall()
        tag = "q" + str(index+1)
        output_result(tag, result)


 #end for
    ## TODO problem 2
    ## TODO problem 3
    #end run()


if __name__ == '__main__':
    run()