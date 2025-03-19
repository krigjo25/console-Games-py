
-- Creating the table / updating the table categories
CREATE TABLE IF NOT EXISTS categories (

  --  Column labels
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  categories TEXT NOT NULL,
  sub TEXT DEFAULT NULL,
  sub1 TEXT DEFAULT NULL,
  sub2 TEXT DEFAULT NULL,
  sub3 TEXT DEFAULT NULL,
  sub4 TEXT DEFAULT NULL,
  sub5 TEXT DEFAULT NULL,
  sub6 TEXT DEFAULT NULL,
  sub7 TEXT DEFAULT NULL,
  sub8 TEXT DEFAULT NULL,
  sub9 TEXT DEFAULT NULL,
  sub10 TEXT DEFAULT NULL,

  -- Constraints
  UNIQUE(categories));


INSERT INTO 'categories'(categories, sub, sub1, sub2) VALUES 
('Disney', 'Roles', 'Character', 'Anime');

INSERT INTO 'categories'(categories) VALUES 
('Random');

CREATE TABLE IF NOT EXISTS disney (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  character TEXT NOT NULL,
  roles TEXT NOT NULL,
  anime Name TEXT NOT NULL,

  --  Constraints
  UNIQUE(`Name`)
);

INSERT INTO `disney` VALUES
(1,'Aladdin','Hero','Aladdin'),
(2,'Clayton','Villian','Tarzan'),
(3,'Simba','Hero',' The Lion King'),
(4,'Robin Hood','Hero','Robin Hood'),
(5,'Pinhoccio','Hero','Pinocchio'),
(6,'Tarzan','Hero','Tarzan'),
(7,'Quasimodo','Hero','The Hunchback Of Notredame'),
(8,'Hercules','Hero','Hercules'),
(9,'The Beast','Hero',' The Beauti And the Beast'),
(10,'Jasmine','Princess','Aladdin'),
(11,'Mulan','Princess','Mulan'),
(12,'Ariel','Princess',' The Little Marmaid'),
(13,'Aurora','Princess','Sleeping Beauti'),
(14,'Belle','Princess','Beauti And The Beast'),
(15,'Cinderella','Princess',' Cinderella'),
(16,'Merida','Princess','Brave'),
(17,'Moana','Princess',' Moana'),
(18,'Snow White','Princess','Snow White And the Seven Dwarfs'),
(19,'Tiana','Princess','The Princess And The Frog'),
(20,'Rapunzel','Princess','Rapunzel'),
(21,'Govenor John Ratcliff','Villain','Pocahontas'),
(22,'Maleficent','Villian','Sleeping Beauti'),
(23,'The Wicked Queen','Villian','Snow White and the Seven Dwarfs'),
(24,'Lady Tremaine','Villian','Cinderella'),
(25,'Jafar','Villian','Aladdin'),
(26,'Scar','Villian','The Lion King'),
(27,'Ursurella','Villian','The little Marmaid'),
(28,'Dr.Farciller','Villian','The Princess And The Frog'),
(29,'Judge Claude Frollo','Villian','The Hunchback Of Notredame'),
(30,'Mother Gothel','Villian','Rapunzel'),
(31,'Shan Yu','Villian','Mulan'),
(32,'Mor''du','Villian',' Brave'),
(33,'Hades','Villian','Hercules'),
(34,'Gideon','Villian','Pinocchio'),
(35,'Gaston','Villian','The Beauti And The Beast');