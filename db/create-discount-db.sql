create table campaigns (
       campaign_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       brand_id INT,
       description TEXT,
       number_of_codes INT NOT NULL
);
create table discounts (
       campaign_id INT NOT NULL,
       brand_id INT NOT NULL,
       user_id INT NOT NULL,
       discount_code INT NOT NULL,
       is_used BOOLEAN NOT NULL DEFAULT FALSE,
PRIMARY KEY (brand_id, discount_code)
);
create table users (
       user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       user_email TEXT
);

insert into campaigns (brand_id, description, number_of_codes) values (1, 'A great discount', 100);
insert into users (user_email) values ('john.doe@nothing.com');

