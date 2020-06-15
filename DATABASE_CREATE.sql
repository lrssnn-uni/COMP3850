CREATE TABLE Programs (
    id INTEGER PRIMARY KEY, 
    name TEXT
);

CREATE TABLE Courses (
    id INTEGER PRIMARY KEY, 
    course_code TEXT, 
    name TEXT, 
    year_level INTEGER
);

CREATE TABLE Course_In_Program (
    program_id INTEGER, 
    course_id INTEGER, 
    directed_group INTEGER,
    FOREIGN KEY(program_id) REFERENCES Programs(id),
    FOREIGN KEY(course_id) REFERENCES Courses(id)
);

CREATE TABLE Course_Precedence (
    course_before_id INTEGER, 
    course_after_id INTEGER, 
    requirement_group INTEGER, 
    hard INTEGER,
    FOREIGN KEY(course_before_id) REFERENCES Courses(id),
    FOREIGN KEY(course_after_id) REFERENCES Courses(id)
);

CREATE TABLE Directed_Course_Requirements (
    program_id INTEGER, 
    directed_group INTEGER, 
    number_required INTEGER,
    FOREIGN KEY(program_id) REFERENCES Programs(id)
);

INSERT INTO Programs VALUES(1,'Computer Science (Cyber Security Major)');
INSERT INTO Programs VALUES(2,'Information Technology (Business Technology Major)');

INSERT INTO Courses VALUES(1,'COMP1010','Computing Fundamentals',1);
INSERT INTO Courses VALUES(2,'MATH1110','Mathematics for Engineering, Science and Technology 1',1);
INSERT INTO Courses VALUES(3,'SENG1110','Object Oriented Programming',1);
INSERT INTO Courses VALUES(4,'COMP1140','Database and Information Management',1);
INSERT INTO Courses VALUES(5,'MATH1510','Discrete Mathematics',1);
INSERT INTO Courses VALUES(6,'SENG1120','Web Technologies',1);
INSERT INTO Courses VALUES(7,'SENG2130','Systems Analysis and Design',2);
INSERT INTO Courses VALUES(8,'COMP2270','Theory of Computation',2);
INSERT INTO Courses VALUES(9,'INFT2031','Systems and Network Administration',2);
INSERT INTO Courses VALUES(10,'COMP3260','Data Security',3);
INSERT INTO Courses VALUES(11,'COMP2230','Algorithms',2);
INSERT INTO Courses VALUES(12,'COMP2240','Operating Systems',2);
INSERT INTO Courses VALUES(13,'SENG2250','System and Network Security',2);
INSERT INTO Courses VALUES(14,'SENG2260','Human-Computer Interaction',2);
INSERT INTO Courses VALUES(15,'INFT3800','Professional Practice in Information Technology',3);
INSERT INTO Courses VALUES(16,'COMP3851A','Computer Science and Information Technology Work Integrated Learning Part A',3);
INSERT INTO Courses VALUES(17,'COMP3500','Security Attacks: Analysis and Mitigation Strategies',3);
INSERT INTO Courses VALUES(18,'COMP3851B','Computer Science and Information Technology Work Integrated Learning Part B',3);
INSERT INTO Courses VALUES(19,'ELEC3500','Telecommunication Networks',3);
INSERT INTO Courses VALUES(20,'COMP3600','Security Standards and Practices in Industry',3);
INSERT INTO Courses VALUES(21,'INFT2051','Mobile Application Programming',2);
INSERT INTO Courses VALUES(22,'COMP3330','Machine Intelligence',3);
INSERT INTO Courses VALUES(23,'COMP3340','Data Mining',3);
INSERT INTO Courses VALUES(24,'COMP3350','Advanced Database',3);
INSERT INTO Courses VALUES(25,'INFT3100','Project Management',3);
INSERT INTO Courses VALUES(26,'INFT3050','Web Programming',3);
INSERT INTO Courses VALUES(27,'SENG3320','Software Verification and Validation',3);
INSERT INTO Courses VALUES(28,'SENG4430','Software Quality',4);
INSERT INTO Courses VALUES(29,'INFT1004','Introduction to Programming',1);
INSERT INTO Courses VALUES(30,'SENG1050','Web Technologies',1);
INSERT INTO Courses VALUES(31,'INFT2150','Business Analysis',2);
INSERT INTO Courses VALUES(32,'STAT1060','Business Decision Making',1);
INSERT INTO Courses VALUES(33,'EBUS3030','Business Intelligence',3);
INSERT INTO Courses VALUES(34,'EBUS3050','The Digital Economy',3);
INSERT INTO Courses VALUES(35,'ACFI1001','Accounting for Decision Makers',1);
INSERT INTO Courses VALUES(36,'ACFI1002','Accounting Practice',1);
INSERT INTO Courses VALUES(37,'ECON1001','Microeconomics for Business Decisions',1);
INSERT INTO Courses VALUES(38,'ECON1002','Macroeconomics in the Global Economy',1);
INSERT INTO Courses VALUES(39,'MKTG1001','Foundations of Marketing',1);
INSERT INTO Courses VALUES(40,'MNGT1001','Introduction to Management',1);
INSERT INTO Courses VALUES(41,'MNGT1002','Introduction to Entrepeneurship and Innovation',1);
INSERT INTO Courses VALUES(42,'CMNS2140','Principles of Public Relations',2);
INSERT INTO Courses VALUES(43,'IRHR2270','Introduction to Human Resource Management',2);
INSERT INTO Courses VALUES(44,'MNGT2002','Business Venturing',2);
INSERT INTO Courses VALUES(45,'MNGT2005','Leadership and Ethics',2);
INSERT INTO Courses VALUES(46,'IRHR3035','Managing Diversity',3);
INSERT INTO Courses VALUES(47,'MNGT3002','Knowledge Management',3);
INSERT INTO Courses VALUES(48,'MNGT3008','Advanced Innovation Management',3);
INSERT INTO Courses VALUES(49,'MNGT3011','Leading Organisational Change',3);
INSERT INTO Courses VALUES(50,'MNGT3012','Strategic Business Management',3);
INSERT INTO Courses VALUES(51,'ELEC2720','Introduction to Embedded Computing',2);
INSERT INTO Courses VALUES(52,'INFT1150','Foundations of Information Systems',1);
INSERT INTO Courses VALUES(53,'INFT2012','Application Programming',2);
INSERT INTO Courses VALUES(54,'CMNS1090','Media Storytelling',1);

INSERT INTO Course_In_Program VALUES(1,1,0);
INSERT INTO Course_In_Program VALUES(1,2,0);
INSERT INTO Course_In_Program VALUES(1,3,0);
INSERT INTO Course_In_Program VALUES(1,4,0);
INSERT INTO Course_In_Program VALUES(1,5,0);
INSERT INTO Course_In_Program VALUES(1,6,0);
INSERT INTO Course_In_Program VALUES(1,7,0);
INSERT INTO Course_In_Program VALUES(1,8,0);
INSERT INTO Course_In_Program VALUES(1,9,0);
INSERT INTO Course_In_Program VALUES(1,10,0);
INSERT INTO Course_In_Program VALUES(1,11,0);
INSERT INTO Course_In_Program VALUES(1,12,0);
INSERT INTO Course_In_Program VALUES(1,13,0);
INSERT INTO Course_In_Program VALUES(1,14,0);
INSERT INTO Course_In_Program VALUES(1,15,0);
INSERT INTO Course_In_Program VALUES(1,16,0);
INSERT INTO Course_In_Program VALUES(1,17,0);
INSERT INTO Course_In_Program VALUES(1,18,0);
INSERT INTO Course_In_Program VALUES(1,19,0);
INSERT INTO Course_In_Program VALUES(1,20,0);
INSERT INTO Course_In_Program VALUES(1,30,0);
INSERT INTO Course_In_Program VALUES(1,21,1);
INSERT INTO Course_In_Program VALUES(1,22,1);
INSERT INTO Course_In_Program VALUES(1,23,1);
INSERT INTO Course_In_Program VALUES(1,24,1);
INSERT INTO Course_In_Program VALUES(1,25,1);
INSERT INTO Course_In_Program VALUES(1,26,1);
INSERT INTO Course_In_Program VALUES(1,27,1);
INSERT INTO Course_In_Program VALUES(1,28,1);
INSERT INTO Course_In_Program VALUES(2,3,1);
INSERT INTO Course_In_Program VALUES(2,29,1);
INSERT INTO Course_In_Program VALUES(2,1,0);
INSERT INTO Course_In_Program VALUES(2,4,0);
INSERT INTO Course_In_Program VALUES(2,7,0);
INSERT INTO Course_In_Program VALUES(2,9,0);
INSERT INTO Course_In_Program VALUES(2,14,0);
INSERT INTO Course_In_Program VALUES(2,15,0);
INSERT INTO Course_In_Program VALUES(2,16,0);
INSERT INTO Course_In_Program VALUES(2,18,0);
INSERT INTO Course_In_Program VALUES(2,25,0);
INSERT INTO Course_In_Program VALUES(2,30,0);
INSERT INTO Course_In_Program VALUES(2,31,0);
INSERT INTO Course_In_Program VALUES(2,24,1);
INSERT INTO Course_In_Program VALUES(2,32,0);
INSERT INTO Course_In_Program VALUES(2,33,0);
INSERT INTO Course_In_Program VALUES(2,34,0);
INSERT INTO Course_In_Program VALUES(2,35,1);
INSERT INTO Course_In_Program VALUES(2,36,1);
INSERT INTO Course_In_Program VALUES(2,37,1);
INSERT INTO Course_In_Program VALUES(2,38,1);
INSERT INTO Course_In_Program VALUES(2,39,1);
INSERT INTO Course_In_Program VALUES(2,40,1);
INSERT INTO Course_In_Program VALUES(2,41,1);
INSERT INTO Course_In_Program VALUES(2,42,1);
INSERT INTO Course_In_Program VALUES(2,43,1);
INSERT INTO Course_In_Program VALUES(2,44,1);
INSERT INTO Course_In_Program VALUES(2,45,1);
INSERT INTO Course_In_Program VALUES(2,46,1);
INSERT INTO Course_In_Program VALUES(2,47,1);
INSERT INTO Course_In_Program VALUES(2,48,1);
INSERT INTO Course_In_Program VALUES(2,49,1);
INSERT INTO Course_In_Program VALUES(2,50,1);

INSERT INTO Course_Precedence VALUES(3,6,0,0);
INSERT INTO Course_Precedence VALUES(3,7,1,0);
INSERT INTO Course_Precedence VALUES(1,7,1,0);
INSERT INTO Course_Precedence VALUES(5,8,0,0);
INSERT INTO Course_Precedence VALUES(6,8,0,0);
INSERT INTO Course_Precedence VALUES(30,9,0,0);
INSERT INTO Course_Precedence VALUES(3,10,0,0);
INSERT INTO Course_Precedence VALUES(6,10,0,0);
INSERT INTO Course_Precedence VALUES(5,10,0,0);
INSERT INTO Course_Precedence VALUES(5,11,0,0);
INSERT INTO Course_Precedence VALUES(6,11,0,0);
INSERT INTO Course_Precedence VALUES(6,12,0,0);
INSERT INTO Course_Precedence VALUES(12,13,1,0);
INSERT INTO Course_Precedence VALUES(51,13,1,0);
INSERT INTO Course_Precedence VALUES(9,13,1,0);
INSERT INTO Course_Precedence VALUES(30,14,0,0);
INSERT INTO Course_Precedence VALUES(3,14,1,0);
INSERT INTO Course_Precedence VALUES(29,14,1,0);
INSERT INTO Course_Precedence VALUES(7,15,1,0);
INSERT INTO Course_Precedence VALUES(31,15,1,0);
INSERT INTO Course_Precedence VALUES(9,17,1,0);
INSERT INTO Course_Precedence VALUES(12,17,1,0);
INSERT INTO Course_Precedence VALUES(16,18,0,1);
INSERT INTO Course_Precedence VALUES(6,19,0,0);
INSERT INTO Course_Precedence VALUES(17,20,0,0);
INSERT INTO Course_Precedence VALUES(52,31,0,0);
INSERT INTO Course_Precedence VALUES(4,26,0,0);
INSERT INTO Course_Precedence VALUES(53,26,1,0);
INSERT INTO Course_Precedence VALUES(3,26,1,0);
INSERT INTO Course_Precedence VALUES(4,33,0,0);
INSERT INTO Course_Precedence VALUES(3,33,1,0);
INSERT INTO Course_Precedence VALUES(29,33,1,0);
INSERT INTO Course_Precedence VALUES(35,36,0,0);
INSERT INTO Course_Precedence VALUES(54,42,0,0);
INSERT INTO Course_Precedence VALUES(41,44,0,0);
INSERT INTO Course_Precedence VALUES(35,44,0,0);
INSERT INTO Course_Precedence VALUES(39,44,0,0);
INSERT INTO Course_Precedence VALUES(40,45,0,0);
INSERT INTO Course_Precedence VALUES(4,24,0,0);
INSERT INTO Course_Precedence VALUES(29,24,1,0);
INSERT INTO Course_Precedence VALUES(3,24,1,0);
INSERT INTO Course_Precedence VALUES(43,46,0,0);
INSERT INTO Course_Precedence VALUES(40,47,0,0);
INSERT INTO Course_Precedence VALUES(41,48,0,0);
INSERT INTO Course_Precedence VALUES(40,49,0,0);
INSERT INTO Course_Precedence VALUES(40,50,0,0);
INSERT INTO Course_Precedence VALUES(45,50,0,0);

INSERT INTO Directed_Course_Requirements VALUES(1,1,2);
INSERT INTO Directed_Course_Requirements VALUES(2,1,3);