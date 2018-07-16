import pyhs2

with pyhs2.connect(host='144.131.252.182',port=10000,authMechanism="PLAIN",user='dev_yxlm_dca',password='dev_yxlm_dca',database='yxlm_bizweb') as conn:
  with conn.cursor() as cur:
  #Show databases
    print cur.getDatabases()
  #Execute query
    cur.execute("select * from tbl_ch_org")
  #Return column info from query
    print cur.getSchema()
  #Fetch table results
    for i in cur.fetch():
      print i
