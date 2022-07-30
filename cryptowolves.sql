-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema cryptowolves
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `cryptowolves` ;

-- -----------------------------------------------------
-- Schema cryptowolves
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cryptowolves` DEFAULT CHARACTER SET utf8 ;
USE `cryptowolves` ;

-- -----------------------------------------------------
-- Table `cryptowolves`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cryptowolves`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NULL,
  `username` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `ofAge` TINYINT NULL,
  `legalToTrade` TINYINT NULL,
  `mailingList` TINYINT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cryptowolves`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cryptowolves`.`posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `post` VARCHAR(255) NULL,
  `category` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`, `users_id`),
  INDEX `fk_posts_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_posts_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `cryptowolves`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cryptowolves`.`users_profile`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cryptowolves`.`users_profile` (
  `profile_id` INT NOT NULL AUTO_INCREMENT,
  `profile_name` VARCHAR(45) NULL,
  `profile_about` VARCHAR(255) NULL,
  `profile_favorite_project` VARCHAR(5) NULL,
  `users_id` INT NOT NULL,
  `posts_id` INT NOT NULL,
  `posts_users_id` INT NOT NULL,
  PRIMARY KEY (`profile_id`, `users_id`, `posts_id`, `posts_users_id`),
  INDEX `fk_users_profile_users1_idx` (`users_id` ASC) VISIBLE,
  INDEX `fk_users_profile_posts1_idx` (`posts_id` ASC, `posts_users_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_profile_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `cryptowolves`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_profile_posts1`
    FOREIGN KEY (`posts_id` , `posts_users_id`)
    REFERENCES `cryptowolves`.`posts` (`id` , `users_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
