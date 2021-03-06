class SqlQueries:
    
    League_table_create= ("""
    CREATE TABLE IF NOT EXISTS League (
    id INTEGER PRIMARY KEY  ,
    country_id INTEGER,
    name VARCHAR UNIQUE
    );""")

    Player_table_create= ("""
    CREATE TABLE IF NOT EXISTS Player (
    id INTEGER PRIMARY KEY,
    player_api_id INTEGER UNIQUE,
    player_name VARCHAR,
    player_fifa_api_id INTEGER UNIQUE,
    birthday VARCHAR,
    height NUMERIC,
    weight NUMERIC
    );""")
    
    Player_atrributes_table_create= ("""
    CREATE TABLE IF NOT EXISTS Player_Attributes (
    id INTEGER PRIMARY KEY,
    player_fifa_api_id INTEGER REFERENCES Player(player_fifa_api_id),
    player_api_id INTEGER REFERENCES Player(player_api_id) ,
    date VARCHAR,
    overall_rating Float,
    potential Float,
    preferred_foot VARCHAR,
    attacking_work_rate VARCHAR,
    defensive_work_rate VARCHAR,
    crossing Float,
    finishing Float,
    heading_accuracy Float,
    short_passing Float,
    volleys Float,
    dribbling Float,
    curve Float,
    free_kick_accuracy Float,
    long_passing Float,
    ball_control Float,
    acceleration Float,
    sprint_speed Float,
    agility Float,
    reactions Float,
    balance Float,
    shot_power Float,
    jumping Float,
    stamina Float,
    strength Float,
    long_shots Float,
    aggression Float,
    interceptions Float,
    positioning Float,
    vision Float,
    penalties Float,
    marking Float,
    standing_tackle Float,
    sliding_tackle Float,
    gk_diving Float,
    gk_handling Float,
    gk_kicking Float,
    gk_positioning Float,
    gk_reflexes Float
);""")
    Team_table_create= ("""
CREATE TABLE IF NOT EXISTS Team (
    id INTEGER PRIMARY KEY,
    team_api_id INTEGER UNIQUE,
    team_fifa_api_id FLOAT,
    team_long_name VARCHAR,
    team_short_name VARCHAR
);""")
    
    Team_Attributes_table_create= ("""

CREATE TABLE IF NOT EXISTS Team_Attributes (
    id INTEGER PRIMARY KEY,
    team_fifa_api_id INTEGER,
    team_api_id INTEGER REFERENCES Team(team_api_id),
    date VARCHAR,
    buildUpPlaySpeed NUMERIC,
    buildUpPlaySpeedClass VARCHAR,
    buildUpPlayDribbling NUMERIC,
    buildUpPlayDribblingClass VARCHAR,
    buildUpPlayPassing NUMERIC,
    buildUpPlayPassingClass VARCHAR,
    buildUpPlayPositioningClass VARCHAR,
    chanceCreationPassing NUMERIC,
    chanceCreationPassingClass VARCHAR,
    chanceCreationCrossing NUMERIC,
    chanceCreationCrossingClass VARCHAR,
    chanceCreationShooting NUMERIC,
    chanceCreationShootingClass VARCHAR,
    chanceCreationPositioningClass VARCHAR,
    defencePressure NUMERIC,
    defencePressureClass VARCHAR,
    defenceAggression NUMERIC,
    defenceAggressionClass VARCHAR,
    defenceTeamWidth NUMERIC,
    defenceTeamWidthClass VARCHAR,
    defenceDefenderLineClass VARCHAR
);""")

    Match_table_create= ("""
CREATE TABLE IF NOT EXISTS Match (
    id INTEGER PRIMARY KEY,
    country_id INTEGER REFERENCES Country(id),
    league_id INTEGER REFERENCES League(id),
    season VARCHAR,
    stage INTEGER,
    date VARCHAR,
    match_api_id INTEGER UNIQUE,
    home_team_api_id INTEGER REFERENCES Team(team_api_id),
    away_team_api_id INTEGER REFERENCES Team(team_api_id),
    home_team_goal INTEGER,
    away_team_goal INTEGER,
    home_player_X1 INTEGER REFERENCES Player(id),
    home_player_X2 INTEGER REFERENCES Player(id),
    home_player_X3 INTEGER REFERENCES Player(id),
    home_player_X4 INTEGER REFERENCES Player(id),
    home_player_X5 INTEGER REFERENCES Player(id),
    home_player_X6 INTEGER REFERENCES Player(id),
    home_player_X7 INTEGER REFERENCES Player(id),
    home_player_X8 INTEGER REFERENCES Player(id),
    home_player_X9 INTEGER REFERENCES Player(id),
    home_player_X10 INTEGER REFERENCES Player(id),
    home_player_X11 INTEGER REFERENCES Player(id),
    away_player_X1 INTEGER REFERENCES Player(id),
    away_player_X2 INTEGER REFERENCES Player(id),
    away_player_X3 INTEGER REFERENCES Player(id),
    away_player_X4 INTEGER REFERENCES Player(id),
    away_player_X5 INTEGER REFERENCES Player(id),
    away_player_X6 INTEGER REFERENCES Player(id),
    away_player_X7 INTEGER REFERENCES Player(id),
    away_player_X8 INTEGER REFERENCES Player(id),
    away_player_X9 INTEGER REFERENCES Player(id),
    away_player_X10 INTEGER REFERENCES Player(id),
    away_player_X11 INTEGER REFERENCES Player(id),
    home_player_Y1 INTEGER,
    home_player_Y2 INTEGER,
    home_player_Y3 INTEGER,
    home_player_Y4 INTEGER,
    home_player_Y5 INTEGER,
    home_player_Y6 INTEGER,
    home_player_Y7 INTEGER,
    home_player_Y8 INTEGER,
    home_player_Y9 INTEGER,
    home_player_Y10 INTEGER,
    home_player_Y11 INTEGER,
    away_player_Y1 INTEGER,
    away_player_Y2 INTEGER,
    away_player_Y3 INTEGER,
    away_player_Y4 INTEGER,
    away_player_Y5 INTEGER,
    away_player_Y6 INTEGER,
    away_player_Y7 INTEGER,
    away_player_Y8 INTEGER,
    away_player_Y9 INTEGER,
    away_player_Y10 INTEGER,
    away_player_Y11 INTEGER,
    home_player_1 INTEGER,
    home_player_2 INTEGER,
    home_player_3 INTEGER,
    home_player_4 INTEGER,
    home_player_5 INTEGER,
    home_player_6 INTEGER,
    home_player_7 INTEGER,
    home_player_8 INTEGER,
    home_player_9 INTEGER,
    home_player_10 INTEGER,
    home_player_11 INTEGER,
    away_player_1 INTEGER,
    away_player_2 INTEGER,
    away_player_3 INTEGER,
    away_player_4 INTEGER,
    away_player_5 INTEGER,
    away_player_6 INTEGER,
    away_player_7 INTEGER,
    away_player_8 INTEGER,
    away_player_9 INTEGER,
    away_player_10 INTEGER,
    away_player_11 INTEGER,
    goal VARCHAR,
    shoton VARCHAR,
    shotoff VARCHAR,
    foulcommit VARCHAR,
    card VARCHAR,
    cross_stat VARCHAR,
    corner VARCHAR,
    possession VARCHAR,
    B365H NUMERIC,
    B365D NUMERIC,
    B365A NUMERIC,
    BWH NUMERIC,
    BWD NUMERIC,
    BWA NUMERIC,
    IWH NUMERIC,
    IWD NUMERIC,
    IWA NUMERIC,
    LBH NUMERIC,
    LBD NUMERIC,
    LBA NUMERIC,
    PSH NUMERIC,
    PSD NUMERIC,
    PSA NUMERIC,
    WHH NUMERIC,
    WHD NUMERIC,
    WHA NUMERIC,
    SJH NUMERIC,
    SJD NUMERIC,
    SJA NUMERIC,
    VCH NUMERIC,
    VCD NUMERIC,
    VCA NUMERIC,
    GBH NUMERIC,
    GBD NUMERIC,
    GBA NUMERIC,
    BSH NUMERIC,
    BSD NUMERIC,
    BSA NUMERIC
);""")

    point_table_create= ("""    
    CREATE TABLE IF NOT EXISTS Point(
    match_api_id INTEGER REFERENCES Match(match_api_id),
    home_team_goal INTEGER,
    away_team_goal INTEGER,
    season VARCHAR,
    result VARCHAR,
    name VARCHAR 
);""")

    # CREATE TABLES

    Country_table_create= ("""
    CREATE TABLE IF NOT EXISTS Country (
    id INTEGER PRIMARY KEY,
    name VARCHAR UNIQUE
    );""")