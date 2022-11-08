/*
/usr/local/mysql/bin/mysql -uroot -p
*/
USE COMPANY;

-- a
SELECT 	Fname, Minit, Lname
FROM 	EMPLOYEE 
WHERE 	Sex="M"
ORDER BY	Lname ASC;

-- b
SELECT	Fname, Minit, Lname, Bdate
FROM	EMPLOYEE, DEPARTMENT
WHERE	Dno=Dnumber AND Dname="Research" AND YEAR(Bdate) LIKE "196_";

-- c
SELECT	E1.Fname, E1.Minit, E1.Lname, E2.Fname, E2.Minit, E2.Lname, Dname, Dlocation
FROM	EMPLOYEE AS E1, EMPLOYEE AS E2, DEPARTMENT AS D, DEPT_LOCATIONS AS DL
WHERE	E1.Super_ssn=E2.Ssn AND E1.Dno=D.Dnumber AND D.Dnumber=DL.Dnumber AND E1.Sex="F";

-- d
SELECT	Fname, Minit, Lname, Salary
FROM	EMPLOYEE
WHERE	Super_ssn IN (SELECT Ssn FROM EMPLOYEE WHERE Fname="James" AND Minit="E" AND Lname="Borg");

-- e
SELECT	Dname, AVG(Salary)
FROM	EMPLOYEE, DEPARTMENT
WHERE	Dno=Dnumber
GROUP BY	Dname;

-- f
SELECT	Pname, SUM(Hours)
FROM	PROJECT, WORKS_ON
WHERE	Pno=Pnumber
GROUP BY	Pname
ORDER BY	SUM(Hours) DESC;

-- g
SELECT	Pname, SUM(Hours)
FROM	PROJECT, WORKS_ON
WHERE	Pno=Pnumber
GROUP BY	Pname
HAVING	SUM(Hours)<40;

-- h
SELECT	Fname, Minit, Lname, Ssn
FROM	EMPLOYEE, DEPARTMENT, DEPT_LOCATIONS
WHERE	Dno=DEPARTMENT.Dnumber AND DEPARTMENT.Dnumber=DEPT_LOCATIONS.Dnumber AND Dlocation="Houston" AND Ssn IN
	(SELECT	DISTINCT Ssn
	 FROM	EMPLOYEE, WORKS_ON, PROJECT
	 WHERE	Ssn=Essn AND Pno=Pnumber AND Plocation<>"Houston");

-- i
SELECT	Fname, Minit, Lname
FROM	EMPLOYEE
WHERE	Ssn NOT IN
	(SELECT	Essn
	 FROM	DEPENDENT);

-- j
SELECT	Fname, Minit, Lname
FROM	EMPLOYEE
WHERE	Ssn IN
	(SELECT	Essn
	 FROM	DEPENDENT
	 WHERE	Dependent_name IN
		(SELECT	Dependent_name
		 FROM	DEPENDENT
		 GROUP BY Dependent_name
		 HAVING COUNT(Dependent_name)>1));

-- SOURCE /Users/Prateek/Desktop/UCONN/2020-2021/CSE 4701/Project 1/SQLRetrieval.txt