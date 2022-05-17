# ORGANISER
#### Video Demo:  <URL HERE>
#### Description:

<br>
<p> 
 My idea for this application was to create something that will help me and my girlfriend to not forget 
 about our assignments, and to keep things organised, because that's helping us a lot in studying and
 scheduling or remembering about other activities. Of course there are much better apps already out there
 but it was really fun to work on my own one. I learned a lot through creating this application, I've 
 watched a lot of guides as well as googled a lot of things because this all was new to me and still is, I 
 am still learning a lot of new skills and tricks with creating applications and working with vscode itself 
 like installing commands to paths or using terminal setting up virtual environment or operating with python 
 interpreter. I like minimalism so I decided to keep it simple and do not apply many effects, so it's smooth 
 sharp and dark themed site, because thta's what I personally like. I was having hard time with styling 
 things and placing stuff over pages but after a lot of stack overflow and testing, trying I made it look 
 nice at least for me I hope it really is nice because I was doing my best while developing this application.
</p>
<br> <hr/> <br>
<p>
<h2> Technologies used </h2>
<ul>
    <li> Flask </li>
    <li> Html </li>
    <li> Css </li>
    <li> Python </li>
    <li> Bootstrap </li>
    <li> Sqlite </li>
</ul>
</p>
<br> <hr/>
<p>
<h3>How does my app work?</h3>
<br>
Firstly you register an account that saves in a database. <br>
Then you login with credentials that you gave while registering. <br>
After you login you firstly see index page which welcomes you by your username. <br>
And then you can read a little about me and how to use that page in paragraphs on the left. <br>
Also on the right side of form that lets you add a task you will see <br> how many days are left for
each task (up to 8 tasks which are closest to deadline)  <br>
Here you can also as I mentioned add your tasks. <br> <br>
It works as a simple organising application which lets you add your tasks, assignments, appointments, 
everything you wish and keeps it saved on your account, other user can't see them. It has some cool features 
as hovering on a task to see a deadline or similar stuff I will write about it a bit later. <br>
<hr/><br>
<h2> How to add a task </h2>
Firstly you add a title which works as a pointer to that task (later on you can move task or delete it by 
its title), titles are unique but for every user so there can be same title saved in database many times but 
it will always have different user's id. <br> <br>
Later on there is description where you can include your personal thoughts or 
little additional things regarding your task. <br> <br>
Lastly you set a deadline (date which you want to end a task by) you will see how many days are for each 
task up to 8 of them at the same time in index page and you also can hover over a task in page which I will 
introduce later on to see deadline of every task you have. Also if you move task to done section it will 
disappear from announcments on this page. <br> <br>
</p>
<hr/>
<p>
<h2> Moving </h2>
is a second feature that lets you start a task by moving it from todo to doing (todo -> doing)
and then <br> from doing to done (doing -> done), you are not able to move tasks backwards. <br> <br>
</p>
<hr/>
<p>
<h2>Delete</h2> is last feature that works with tasks, it lets you delete task from database no matter where 
it is, so you can delete even from done table. <br> <br>
</p>
<hr/>
<p>
<h2> Structure </h2>
 Going from top of my explorer I have insides of my package located in folder called <b>organiser</b>. <br>
 Here first folder that is interesting is <b>/static</b> here i keep my css although most of css I used 
 comes from bootstrap because I am not strong in front end at all, I find it hard to work with css and html.
 Then there is <b>/templates</b> where I keep all my html files and I will describe them one by one now.<br> 
 <br>
</p>

<p>
 <b>_messages.html</b> -> Here is little subtemplate for my error annoucnments which I include to each html
 instead of pasting whole code everywhere I just {% include %} it, I could keep it in my base template but t
 hen it would be much harder for me to place divs in my main pages so I decided to make it in subtemplate 
 format.
</p>
</br>
<p>
 <b>base.html</b> -> This is My base template which my other html files are extedning, it keeps basic html 
 structure and a bootstrap navbar as well as my css linking.
</p>
</br>
<p>
 <b>delete.html</b> -> Page holding one of features it is really simple which is to delete tasks that
 we don't want to keep anymore, it also has little instruction for users
</p>
</br>
<p>
 <b>edit_profile.html</b> -> I used this one to let user change their usernames and give a short description 
 if they want to!
</p>
</br>
<p>
 <b>index.html</b> -> Basic page where user starts after logging in, it contains brief descritpion of me and
 my app, it also holds a form by which we can add task, it also has feature which tells you how many days
 are left until deadline that you set while adding task, I wrote little function that counts days by
 taking actual date by datetime.utcnow().date() and then makes a divison with deadline.date() it lets you 
 know how many days are until your deadline for each task.
</p>
</br>
<p>
 <b>login.html</b> -> Name tells by itself, it is just login page with form which after submittin login 
 credentials query for an account and then compare hashes and log user in if they are matching.
</p>
</br>
<p>
 <b>move.html</b> -> Contains one of features which is moving tasks in way todo -> doing, doing -> done
 there is no possibility to move them backwards, if you started doing something, end it!
</p>
</br>
<p>
 <b>register.html</b> -> Here also it says by itself, registration form in html page
</p>
</br>
<p>
 <b>tasks.html</b> -> Page contains table which shows all tasks that user added to the account it is main 
 page of my app where you see what you have to do after you added and moved everything as you wanted to. If 
 you hover on each task you will see date which you have chosen while adding task in deadline field. 
</p>
</br>
<p>
 <b>user.html</b> -> User's page where user can see email username and number of completed tasks also a
 description of user that can be made by the user
</p>
</br>
<p>
 Features are divided to different pages to allow mobile users to use website comfortably as well as 
 computer or laptop users, but I'm too bad with front-end and I designed it only for my laptop.
</p>
<hr/></br>
<p>
 after <b>/template</b> there are python files first one is: <br> <br>
 <b>__init__.py</b> -> file which contains my installed flask extensions which I'm using
 in my applicaiton as well as app itself and imports <br> <br>
</p>

<p>
 <b>forms.py</b> -> file contains all of my forms which I later pass to the following file which is 
 routes.py, it is simple file I just have a lot of files because I was creating my applications
 using divide and conquer strategy which is very useful because my code is not messed up
 as much as it would be. <br> <br>
</p>

<p>
 <b>routes.py</b> -> Contains all of my view functions and python code. Here is located most of my backend
 code which is making my site work. Here i have all functions for example one which contains computing days 
 until end of deadline taking actual date from datetime. I also work with databse by commiting users tasks,
 moving tasks and deleting them from database. <br> <br>
</p>
<hr/>
<p>
Out of package folder we have some other files one is <b>.flaskenv</b> where I simply set my flask 
environmental variables such as FLASK_ENV
</p>
<br>
<p>
<b>application.py</b> -> application file which starts my app and also configures flask shell by which I can 
work with my database and check for errors or test features before implement them in my app
</p>
<br> 
<p>
<b>config.py</b> -> is my configuration file here I create databse connection and configure my variables
</p>
<hr/><br><br>
<p> 
There also is directory called <b>/migrations</b> it keeps migration scripts for my database it lets me 
operate very fast2 while working on my database because these scripts are very easy to understand you write 
what you want in <b>models.py</b> then run command flask db migrate and then flask db upgrade and voila 
database has new tables or rows that you wanted to add. And if my databse doesn't work after it or something 
goes wrong I can very fast use flask db downgrade delete migration script and redo new one by again running 
first two command after making changes to <b>models.py</b>
</p># organiser
