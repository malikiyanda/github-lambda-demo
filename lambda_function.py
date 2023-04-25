from sqlalchemy import create_engine

def lambda_handler(event, context):
     #create DB engine 
     engine = create_engine('postgresql://postgres:testpostgresdb@malik-database.cujukyhtv5pn.us-east-1.rds.amazonaws.com:5432/navitascustomer', connect_args={'options': '-c search_path=customerrequest'})
     