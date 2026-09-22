Roman Numerals Converter – Flask + AWS CloudFormation

A small end-to-end cloud project that converts decimal numbers from 1 to 3999 into Roman numerals.

The application is written in Python, exposed as a Flask web application, stored in GitHub, and deployed to Amazon EC2 using an AWS CloudFormation template.

Project Overview

This project demonstrates the complete path from local development to a running web application in AWS:

Local PC
   ↓
Python + Flask application
   ↓
Git / GitHub
   ↓
AWS CloudFormation
   ↓
Security Group + EC2
   ↓
EC2 UserData
   ↓
Clone GitHub repository
   ↓
Install Flask and dependencies
   ↓
Run application on port 80
   ↓
Public web application

Features

Converts decimal numbers from 1–3999 to Roman numerals

Validates invalid or out-of-range input

Flask-based web interface

Infrastructure defined with CloudFormation

EC2 instance created automatically

HTTP and SSH access configured through a Security Group

Application installation and startup automated with EC2 UserData

Application source cloned automatically from GitHub

CloudFormation output provides the website URL

Example conversions

Decimal

Roman

3

III

9

IX

58

LVIII

1994

MCMXCIV

Technologies Used

Python

Flask

HTML / Jinja

Git

GitHub

AWS EC2

AWS CloudFormation

Amazon Linux 2023

EC2 UserData

AWS Security Groups

Project Structure

roman-numerals-converter/
├── app.py
├── cfn-template.yml
└── templates/
    ├── index.html
    └── result.html

app.py

Contains the Roman numeral conversion logic, Flask routes, input validation, and template rendering.

templates/

Contains the Flask/Jinja HTML pages:

index.html – input form and validation message

result.html – displays the converted Roman numeral

cfn-template.yml

Defines the AWS infrastructure, including:

EC2 instance

Amazon Linux 2023 AMI parameter

t3.micro instance type

EC2 Key Pair parameter

Security Group

HTTP port 80

SSH port 22

EC2 UserData

Website URL output

Deployment Workflow

Create and test the Roman numeral converter locally.

Convert the Python application into a Flask web application.

Create a separate local Git repository.

Push the application to a public GitHub repository.

Create the CloudFormation template.

Upload the template to AWS CloudFormation.

Provide the EC2 Key Pair and Amazon Linux 2023 AMI ID.

Create the CloudFormation stack.

CloudFormation creates the Security Group and EC2 instance.

EC2 UserData installs Git, Python/pip and Flask.

UserData clones this GitHub repository.

Flask starts on port 80.

CloudFormation returns the public website URL in Outputs.

EC2 UserData Automation

When the EC2 instance starts, the CloudFormation UserData script performs the application setup automatically:

#!/bin/bash
dnf update -y
dnf install -y git python3-pip

cd /home/ec2-user
git clone https://github.com/sm2021praktikum/roman-numerals-converter.git

cd roman-numerals-converter
pip3 install flask

nohup python3 app.py > /var/log/roman-app.log 2>&1 &

The Flask application listens on:

app.run(host="0.0.0.0", port=80)

Deployment Evidence

The following screenshots document the completed deployment.

Running Flask Application



CloudFormation Stack – CREATE_COMPLETE



CloudFormation Output



Git Commit History



What I Practiced

This project provided hands-on practice with:

Python application logic

Flask routing and templates

input validation

local application testing

Git version control

GitHub repositories

YAML

infrastructure as code

EC2 provisioning

Security Groups

Linux commands

SSH

EC2 UserData automation

CloudFormation stack creation and troubleshooting

Repository

GitHub: sm2021praktikum/roman-numerals-converter


Built as a hands-on AWS / DevOps learning project.
