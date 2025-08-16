CREATE TABLE Customer (
    cno INT NOT NULL AUTO_INCREMENT,
    cname VARCHAR(40) NOT NULL,
    ano INT,
    password VARCHAR(10) NOT NULL UNIQUE,
    PRIMARY KEY (cno),
    FOREIGN KEY (ano) REFERENCES Agent(ano))

CREATE TABLE Properties (
    propertyid INT NOT NULL AUTO_INCREMENT,
    ano INT,
    rooms INT NOT NULL,
    bathrooms INT NOT NULL,
    kitchen INT NOT NULL,
    price INT NOT NULL,
    scno INT,
    bcno INT,
    status VARCHAR(5) NOT NULL,
    location VARCHAR(100) NOT NULL,
    square_feet BIGINT,
    PRIMARY KEY (propertyid),
    FOREIGN KEY (ano) REFERENCES Agent(ano),
    FOREIGN KEY (scno) REFERENCES Customer(cno),
    FOREIGN KEY (bcno) REFERENCES Customer(cno)
);

CREATE TABLE Agent (
    ano INT NOT NULL AUTO_INCREMENT,
    aname VARCHAR(40) NOT NULL,
    acontact BIGINT NOT NULL,
    agent_password VARCHAR(20) NOT NULL,
    PRIMARY KEY (ano))