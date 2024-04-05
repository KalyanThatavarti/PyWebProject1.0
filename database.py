from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://root:Superman123@pyweb-db.c38c0cqk664a.us-east-2.rds.amazonaws.com/pyweb-db?charset=utf8mb4",
    echo=True)

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    column_names = result.keys()
    result_dicts = []
    for row in result.all():
        result_dicts.append(dict(zip(column_names, row)))
    print(result_dicts)
