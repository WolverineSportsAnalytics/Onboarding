CREATE SCHEMA IF NOT EXISTS `WSA` DEFAULT CHARACTER SET utf8 ;
USE `WSA` ;

-- -----------------------------------------------------
-- Table `WSA`.`nfl`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `WSA`.`NFL` (
	`playerID` int(11) not null, 
	`year` int(11) not null, 
	`playerName` varchar(45),
	`college` varchar(45),
	`position` varchar(45),
	`height` float(11) not null, 
	`weight` float(11) not null, 
	`dash` float(11), 
	`bench` float(11), 
	`leap` float(11), 
	`broad` float(11), 
	`shuttle` float(11), 
	`cone` float(11), 
    Primary Key (playerID)
);

