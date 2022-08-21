import webbrowser,urllib3
from selenium import webdriver
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv, requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chromedriver="C:/Users/ANOM VNM/chromedriver_linux64/chromedriver"
driver=webdriver.Chrome(chromedriver)
driver.get("http://pmms.gtu.ac.in/GTULoginPage")

# new=2
# driver=webdriver.firefox()
# driver.get('http://de.gtu.ac.in/Account/Login')
# url='http://de.gtu.ac.in/Account/Login'

# webbrowser.open(url,new=new)

search_box=driver.find_element(By.ID,'UserName').send_keys('170280117049')
search_box=driver.find_element(By.ID,'Password').send_keys('84624923')



input('press any key to continue')
driver.get("http://pmms.gtu.ac.in/Student/StudentActivity/TLRequestToAddTeamMember")

no=["170170111001","170170111002","170170111003"]
alltabs=driver.window_handles
csvfile=open('dat.csv','w+',newline='')
writer=csv.writer(csvfile)
writer.writerow(['Name','College','Enrollment No','Mobile No','Email Id','Department','Displine','Semester'])
csvRow=[]
xcsvRow=["ashiah balar","vosiw",170280111101,9927819123,"hsjanjw@gmail.com","ic","dw",1]
for tab in alltabs:
    driver.switch_to.window(tab)
    if(driver.current_url=='http://pmms.gtu.ac.in/Student/StudentActivity/TLRequestToAddTeamMember'):        
        for i in range(170170111001,170170111005,1):
            search_box=driver.find_element(By.ID,'ContentPlaceHolder1_txtTeamMemEnrolmentNo')
            search_box.clear()
            search_box.send_keys(i)
            
            driver.find_element(By.XPATH," //input[@id='ContentPlaceHolder1_btnSearchEnrollmentNo']").click()
            sleep(2)

            name=driver.find_element(By.ID,"ContentPlaceHolder1_lblTeamMemName")
            # if(xcsvRow[1]==name.text):
            #     break
            College=driver.find_element(By.ID,"ContentPlaceHolder1_lblTeamMemCollege")
            Enrollment=driver.find_element(By.ID,"ContentPlaceHolder1_lblEnrollmentNo")
            Mobile=driver.find_element(By.ID,"ContentPlaceHolder1_lblTeamMemMobileNo")
            Email=driver.find_element(By.ID,"ContentPlaceHolder1_lblTeamMemEmailId")
            Department=driver.find_element(By.ID,"ContentPlaceHolder1_lblTeamMemDepartment")
            Discipline=driver.find_element(By.ID,"ContentPlaceHolder1_lblTeamMemDiscipline")
            Semester=driver.find_element(By.ID,"ContentPlaceHolder1_lblTeamMemSemester")

            csvRow.append(name.text)
            csvRow.append(College.text)
            csvRow.append(Enrollment.text)
            csvRow.append(Mobile.text)
            csvRow.append(Email.text)
            csvRow.append(Department.text)
            csvRow.append(Discipline.text)
            csvRow.append(Semester.text)
            writer.writerow(csvRow)
            # xcsvRow=csvRow
            # print(csvRow[1])
            # print(xcsvRow[2])
            csvRow.clear()
        
csvfile.close()
driver.quit()