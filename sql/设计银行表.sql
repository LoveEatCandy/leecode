-- noinspection SqlNoDataSourceInspectionForFile

-- [Database model design] Design a database model for a bank:
-- There are multiple branches under a head office, and each branch provides savings and loan services to customers.
-- A customer can open accounts and apply for loans under different branches.
-- Briefly write down the tables needed(including fields).


CREATE TABLE `bank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(56) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `branch_bank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bank_id` int(11) DEFAULT NULL,
  `name` varchar(56) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(56) DEFAULT NULL,
  `saved_money` decimal(20, 2) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `save_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` int(11) DEFAULT NULL,
  `branch_bank_id` int(11) DEFAULT NULL,
  `money` decimal(20, 2) DEFAULT NULL,
  `trade_type` int(11) DEFAULT NULL, -- 枚举类型：取款、存款
  PRIMARY KEY (`id`)
);

CREATE TABLE `loan_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` int(11) DEFAULT NULL,
  `branch_bank_id` int(11) DEFAULT NULL,
  `money` decimal(20, 2) DEFAULT NULL,
  `status` int(11) DEFAULT NULL, -- 枚举类型：未还款、已还款
  PRIMARY KEY (`id`)
);