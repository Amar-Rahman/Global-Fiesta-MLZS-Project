import pickle

def display(x):
    global movie_database
    print("=" * 100)
    print(" "*20 + x.upper() + " " * 20)
    print("Year Released: ", movie_database[x][1])
    print("Genre: ")
    for m in movie_database[x][2]:
        print(m, end=", ")
    print(" ")
    print("Cast: ")
    for n in movie_database[x][3]:
        print(n, end=", ")
    print(" ")
    print("Director: ", movie_database[x][4])
    print("Box Office Earnings: ", movie_database[x][5])
    print("=" * 100)


def average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t
    avg = sum_num / len(num)
    return avg


def user_display(x):
    global movie_database
    print("=" * 100)
    print(" " * 20 + x.upper() + " " * 20)
    print("Year Released: ", movie_database[x][1])
    print("Genre: ")
    for m in movie_database[x][2]:
        print(m, end=", ")
    print("Ratings: ")
    if movie_database[x][6] == []:
        print('No Reviews Yet')
    else:
        print(round(average(movie_database[x][6]), 1), "/10")
    print(" ")
    print("Cast: ")
    for n in movie_database[x][3]:
        print(n, end=", ")
    print(" ")
    print("Director:", movie_database[x][4])
    print("Box Office Earnings", movie_database[x][5])
    print("Would you like to give a rating?(Yes/No): ")
    rating_choice = input()
    if rating_choice == "Yes":
        rating = int(input("Rating between 1 and 10: "))
        movie_database[x][6].append(rating)
    print("=" * 100)
user_login_details = {"username123":"abcd", "username456":"password" ,"username789":"helloworld"}
admin_login_details = {"admin123":"adminabcd", "admin456":"adminpassword", "admin789":"adminhelloworld"}

username = input("Enter Username: ")
password = input("Enter Password: ")
if username in user_login_details and password == user_login_details[username]:
    usertype = "user"
if username in admin_login_details and password == admin_login_details[username]:
    usertype = "admin"
if usertype != "admin" and usertype != "user":
    print("invalid login credentials")


movie_database = {'Baadshah': ['Baadshah', '1999', ['Comedy', 'Musical'], ['Shah Rukh Khan', 'Twinkle Khanna'], 'Abbas Burmawalla', '31.6 crores', []], 'Yes Boss': ['Yes Boss', '1997', ['Romance', 'Musical'], ['Shah Rukh Khan'], 'Aziz Mirza', '23 Crores', []], 'Karan Arjun': ['Karan Arjun', '1995', ['Action', 'Fantasy'], ['Shah Rukh Khan', 'Kajol'], 'Rakesh Roshan', '45 crores', []], 'Ram Jaane': ['Ram Jaane', '1995', ['Action'], ['Shah Rukh Khan', 'Juhi Chawla'], 'Rajiv Mehra', '15.19 Crores', []], 'Happy New Year': ['Happy New Year', '2014', ['Action', 'Musical'], ['Shah Rukh Khan', 'Deepika Padukone'], 'Farah Khan', '408 Crores', []], 'Badla': ['Badla', '2019', ['Thriller', 'Drama'], ['Shah Rukh Khan', 'Amitabh Bachchan'], 'Sujay Ghosh', '13.84 Crores', []], 'Main Hoon Na': ['Main Hoon Na', '2004', ['Romance'], ['Shah Rukh Khan', 'Sushmita Sen'], 'Farah Khan', '1.2 Crores', []], 'Dil Se': ['Dil Se', '1998', ['Romance', 'Musical'], ['Shah Rukh Khan', 'Preity Zinda'], 'Mani Ratnam', '28.26 Crores', []], 'Daar': ['Daar', '1993', ['Romance', 'Thriller'], ['Shah Rukh Khan', 'Juhi Chawla'], 'Yash Chopra', '21.31 Crore', []], 'Anjaan': ['Anjaan', '1994', ['Drama'], ['Shah Rukh Khan', 'Madhuri Dixit'], 'Rahul Rawail', '9.66 Crores', []], 'Pardes': ['Pardes', '1997', ['Romance', 'Musical'], ['Shah Rukh Khan', 'Mahima Choudary'], 'Subhash Ghai', '40.95 Crores', []], 'Kuch Kuch Hota Hai': ['Kuch Kuch Hota Hai', '1998', ['Romance', 'Musical'], ['Shah Rukh Khan', 'Kajol', 'Rani Mukherji'], 'Karan Johar', '17 Crores', []], 'Dil To Pagal Hai': ['Dil To Pagal Hai', '1997', ['Romance', 'Musical'], ['Shah Rukh Khan', 'Madhuri Dixit', 'Karishma Kapoor'], 'Yash Chopra', '59 Crores', []], 'Asoka': ['Asoka', '2001', ['Drama', 'Romance'], ['Shah Rukh Khan', 'Kareena Kapoor'], 'Santosh Sivan', '11.54 Crores', []], 'Fan': ['Fan', '2016', ['Thriller', 'Drama'], ['Shah Rukh Khan', 'Shriya Pilgonkar'], 'Maneesh Sharma', '188 Crores', []], 'Duplicate': ['Duplicate', '1998', ['Crime', 'Comedy'], ['Shah Rukh Khan', 'Juhi Chawla'], 'Mahesh Bhatt', '21.49 crores', []], 'Chennai Express': ['Chennai Express', '2013', ['Action', 'Comedy', 'Romance'], ['Shah Rukh Khan', 'Deepika Padukone'], 'Rohit Shetty', '456 Crores', []], 'Bhoothnath Returns': ['Bhoothnath Returns', '2014', ['Horror', 'Comedy'], ['Shah Rukh Khan', 'Amitabh Bachchan'], 'Nitesh Tiwar', '153 Crores', []], 'Raees': ['Raees', '2017', ['Action', 'Drama'], ['Mahira Khan'], 'Rahul Dholkia', '281 Crores', []], 'Zero': ['Zero', '2018', ['Romance', 'Comedy'], ['Shah Rukh Khan', 'Anushka Sharma', 'Katrina Kaif'], 'Aanand.C.Rai', '186 Crores', []], 'Zoya Factor': ['Zoya Factor', '2019', ['Romance', 'Comedy', 'Drama'], ['Shah Rukh Khan', 'Sonam Kapoor', 'Dulquer Salmaan'], 'Abishek Sharma', '6.96 Crores', []], 'Jab Harry Met Sejal': ['Jab Harry Met Sejal', '2017', ['Romance', 'Comedy'], ['Shah Rukh Khan', 'Anushka Sharma'], 'Imtiaz Ali', '153 Crores', []], 'Swades': ['Swades', '2004', ['Drama'], ['Shah Rukh Khan', 'Gayatri'], 'Ashatosh Gowarikar', '36 Crores', []], 'Veer Zaara': ['Veer Zaara', '2004', ['Romance', 'Drama'], ['Shah Rukh Khan', 'Preity Zinda'], 'Yash Chopra', '97.6 Crores', []], 'Ra.One': ['Ra.One', '2013', ['Sci-Fi', 'Drama', 'Action'], ['No', 'Anubhav Sinha'], '207 Crores', '207 Crores', []], 'Don 2': ['Don 2', '2011', ['Action', 'Thriller'], ['Shah Rukh Khan', 'Priyanka Chopra'], 'Farhan AKthar', '203 Crores', []], 'My Name Is Khan': ['My Name Is Khan', '2010', ['Drama'], ['Shah Rukh Khan'], 'Karan Johar', '223 Crores', []]}
movie_database_file = open("movie_database.dat", "wb+")
print("number of movies on database:", len(movie_database))


genre_list = ["Action", "Adventure", "Animation", "Biography", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "Film Noir", "History", "Horror", "Music", "Musical", "Mystery", "Romance", "Sci-Fi", "Short Film", "Sport", "Superhero", "Thriller", "War", "Western"]
if usertype == "admin":

     print("Welcome admin", username)
     admin_check = "Yes"
     while admin_check == "Yes":
         print("To add a new movie, Type 1")
         print("To edit an existing movie's details, Type 2")
         print("To delete a movie from the database, Type 3")
         print("To search for a movie, Type 4")
         print("To log out, Type 5")
         admin_choice= int(input())
         if admin_choice == 1:
             while admin_choice == 1:
                 movie_details = []
                 movie_name = input("Movie Name: ")
                 movie_details.append(movie_name)
                 release_date = input("Release Date: ")
                 movie_details.append(release_date)
                 d = "Yes"
                 genres = []
                 while d == "Yes":
                     genre = input("Genre: ")
                     if genre not in genre_list:
                         print("Invalid Genre")
                         d = "Yes"
                     if genre in genre_list:
                        genres.append(genre)
                        d = input("Add another genre?(Yes/No): ")
                 movie_details.append(genres)
                 print("Cast Members")
                 cast_list = []
                 cast_count = "Yes"
                 while cast_count == "Yes":
                     cast_member = input("Enter Cast member name: ")
                     cast_list.append(cast_member)
                     cast_count = input("Add more cast members?(Yes/No): ")
                 movie_details.append(cast_list)
                 director = input("Director Name: ")
                 movie_details.append(director)
                 box_office_value = input("Box Office Value: ")
                 movie_details.append(box_office_value)
                 rating=[]
                 movie_details.append(rating)
                 movie_database[movie_name] = movie_details


                 display(movie_name)
                 c = input("Add another movie?(Yes/No): ")
                 if c == "Yes":
                     admin_choice = 1
                 else:
                     break
         if admin_choice == 2:
             while admin_choice == 2:
                 print("Which movie would you like to edit (If you wish to exit the editing interface, please type in 'exit'): ")
                 edit_movie = input()
                 if edit_movie == "exit":
                     break
                 if edit_movie not in movie_database:
                     print("This movie is not in the database, try again.")
                     continue
                 if edit_movie in movie_database:
                     display(edit_movie)
                     print("What would you like to edit?: ")
                     print("Movie Name? Type 1")
                     print("Release year? Type 2")
                     print("Genre? Type 3")
                     print("Cast? Type 4")
                     print("Director? Type 5")
                     print("Box office earnings? Type 6")
                     print("to exit editing interface, Type 7")
                     edit_choice = int(input())
                     if edit_choice == 1:
                         while edit_choice == 1:
                             new_movie_name = input("New Movie name?: ")
                             movie_database[edit_movie][0] = new_movie_name
                             movie_database[new_movie_name] = movie_database[edit_movie]
                             movie_database.pop(edit_movie)
                             display(new_movie_name)
                             print("What would you like to edit next?")
                             print("Movie Name? Type 1")
                             print("Release year? Type 2")
                             print("Genre? Type 3")
                             print("Cast? Type 4")
                             print("Director? Type 5")
                             print("Box office earnings? Type 6")
                             print("To exit editing interface, Type 7")
                             edit_choice = int(input())
                     if edit_choice == 2:
                         while edit_choice == 2:
                             movie_database[edit_movie][1] = input("Enter new year")
                             display(edit_movie)
                             print("What would you like to edit next?")
                             print("Movie Name? type 1")
                             print("Release year? type 2")
                             print("Genre? type 3")
                             print("Cast? type 4")
                             print("Director? type 5")
                             print("Box office earnings? type 6")
                             print("to exit editing interface, type 7")
                             edit_choice = int(input())
                     if edit_choice == 3:
                         while edit_choice == 3:
                             print("Current genres are")
                             for i in movie_database[edit_movie][2]:
                                 print(i)
                             genre_edit_loop = "Yes"
                             while genre_edit_loop == "Yes":
                                 print("To delete a genre, Type 1")
                                 print("To add a genre, Type 2")
                                 genre_edit = int(input())
                                 if genre_edit == 1:
                                     print("Enter genre to be deleted:")
                                     genre_delete = input()
                                     if genre_delete in movie_database[edit_movie][2]:
                                         movie_database[edit_movie][2].remove(genre_delete)
                                         print("New Genres")
                                         for i in movie_database[edit_movie][2]:
                                             print(i)
                                     else:
                                         print(genre_delete, "Not in current genre list")
                                 if genre_edit == 2:
                                     genre_add = input("New genre")
                                     if genre_add not in genre_list:
                                         print("invalid genre")
                                     else:
                                         movie_database[edit_movie][2].append(genre_add)
                                 display(edit_movie)
                                 genre_edit_loop = input("Would you like to add more changes?(Yes/No): ")
                                 if genre_edit_loop == "No":
                                     print("What would you like to edit next?")
                                     print("Movie Name? type 1")
                                     print("Release year? type 2")
                                     print("Genre? type 3")
                                     print("Cast? type 4")
                                     print("Director? type 5")
                                     print("Box office earnings? type 6")
                                     print("To exit editing interface, type 7")
                                     edit_choice = int(input())

                     if edit_choice == 4:
                         while edit_choice == 4:
                             print("Current cast members are:")
                             for i in movie_database[edit_movie][3]:
                                 print(i)
                             cast_edit_loop = "Yes"
                             while cast_edit_loop == "Yes":
                                 print("To delete a cast member, type 1")
                                 print("To add a cast member, type 2")
                                 cast_edit = int(input())
                                 if cast_edit == 1:
                                     print("enter cast member to be deleted")
                                     cast_delete = input()
                                     if cast_delete in movie_database[edit_movie][3]:
                                         movie_database[edit_movie][3].remove(cast_delete)
                                         print("New Cast Members")
                                         for i in movie_database[edit_movie][3]:
                                             print(i)
                                     else:
                                         print(cast_delete, "Not in current cast list")
                                 if cast_edit == 2:
                                     cast_add = input("New cast member")
                                     movie_database[edit_movie][3].append(cast_add)
                                 display(edit_movie)
                                 cast_edit_loop = input("Would you like to add more changes?(Yes/No)")
                                 if cast_edit_loop == "No":
                                     print("What would you like to edit next?")
                                     print("Movie Name? type 1")
                                     print("Release year? type 2")
                                     print("Genre? type 3")
                                     print("Cast? type 4")
                                     print("Director? type 5")
                                     print("Box office earnings? type 6")
                                     print("to exit editing interface, type 7")
                                     edit_choice = int(input())
                         if edit_choice == 5:
                             display(edit_movie)
                             movie_database[edit_movie][4] = input("New Director?")
                             display(edit_movie)
                             print("What would you like to edit next?")
                             print("Movie Name? type 1")
                             print("Release year? type 2")
                             print("Genre? type 3")
                             print("Cast? type 4")
                             print("Director? type 5")
                             print("Box office earnings? type 6")
                             print("To exit editing interface, type 7")
                             edit_choice = int(input())

                         if edit_choice == 6:
                             display(edit_movie)
                             movie_database[edit_movie][5] = input("Box Office Earnings?: ")
                             display(edit_movie)
                             print("What would you like to edit next?")
                             print("Movie Name? type 1")
                             print("Release year? type 2")
                             print("Genre? type 3")
                             print("Cast? type 4")
                             print("Director? type 5")
                             print("Box office earnings? type 6")
                             print("To exit editing interface, type 7")
                             edit_choice = int(input())
         if admin_choice == 3:
             delete_movie = input("Enter movie to be deleted")
             movie_database.pop(delete_movie, "The Movie is not in the Database")

         if admin_choice == 4:
            print("How would you like to search for your movie?")
            print("To search using filters, type 1")
            print("To search using name, type 2")
            print("To browse the entire database, type 3")
            searchchoice = int(input())
            if searchchoice == 1:
                print("Filters available are:")
                print("Year or Genre")
                filter_choice = input()
                if filter_choice == "Genre":
                    print("Genres are: ")
                    for i in genre_list:
                        print(i)
                    genre_selection=input("Enter preferred genre: ")
                    for r in movie_database:
                        if genre_selection in movie_database[r][2]:
                            user_display(r)
                if filter_choice == "Year":
                    year_selection=(input("Enter a year: "))
                    for v in movie_database:
                        if year_selection == movie_database[v][1]:
                            user_display(v)
            if searchchoice == 2:
                x = "Yes"
                while x == "Yes":
                    search = input("Enter Name of Movie: ")
                    if search in movie_database:
                        user_display(search)

                    else:
                        print("invalid search")
                    x = input("would you like to search again?(Yes/No)")

            if searchchoice == 3:
                for x in sorted(movie_database.items()):
                    user_display(x[0])

         if admin_choice == 5:
             print("Thank you for visiting our site, please come again")

             print(movie_database)

             break

if usertype == "user":
    print("welcome user", username)
    user_check = "Yes"
    while user_check == "Yes":
        print("To search for a movie, type 1")
        print("To log out, type 2")
        user_choice= int(input())
        if user_choice == 1:
            print("How would you like to search for your movie?")
            print("To search using filters, type 1")
            print("To search using name, type 2")
            print("To browse the entire database, type 3")
            searchchoice = int(input())
            if searchchoice == 1:
                print("Filters available are:")
                print("Year or Genre")
                filter_choice = input()
                if filter_choice == "Genre":
                    print("genres are")
                    for i in genre_list:
                        print(i)
                    genre_selection = input("Enter preferred genre")
                    for r in movie_database:
                        if genre_selection in movie_database[r][2]:
                            user_display(r)
                if filter_choice == "Year":
                    year_selection = (input("Enter a year"))
                    for v in movie_database:
                        if year_selection == movie_database[v][1]:
                            user_display(v)
            if searchchoice == 2:
                x = "Yes"
                while x == "Yes":
                    search = input("Enter Name of Movie")
                    if search in movie_database:
                        user_display(search)

                    else:
                        print("invalid search")
                    x = input("would you like to search again?(Yes/No)")

            if searchchoice == 3:
                for x in sorted(movie_database.items()):
                    user_display(x[0])

        if user_choice == 2:
             print("Thank you for visiting our site, please come again")
             pickle.dump(movie_database, movie_database_file)
             print(movie_database)

             break

























