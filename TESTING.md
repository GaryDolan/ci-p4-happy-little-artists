# Happy Little Artists Art Club

Testing of app was ongoing throughout the development process. I used the developer tools in chrome and firefox to test all aspect of the app.

![Preview of website on various devices](documentation/images/responsive-design-screenshot.png)

# Table of Contents

-   [User story testing](#user-story-testing)
    -   [Owner/Admin & Developer goals](#owneradmin--developer-goals)
    -   [First time visitor goals](#first-time-visitor-goals)
    -   [Returning visitor goals](#returning-visitor-goals)
-   [Automated testing](#automated-testing)
    -   [Python](#python)
    -   [HTML](#html)
    -   [CSS](#css)
    -   [JavaScript](#javascript)
-   [Lighthouse testing](#lighthouse-testing)
-   [Manual testing](#manual-testing)
    -   [Header brand](#header-brand)
    -   [Navigation](#navigation)
    -   [Footer](#footer)
    -   [Home Page](#home-page)
    -   [About Us Page](#about-us-page)
    -   [Sign up Page](#sign-up-page)
    -   [Sign in Page](#sign-in-page)
    -   [Log out Page](#log-out-page)
    -   [Profile Page](#profile-page)
    -   [Empty Profile](#empty-profile)
    -   [Edit Info Page](#edit-info-page)
    -   [Edit Profile Page](#edit-profile-page)
    -   [Edit Booking Page](#edit-booking-page)
    -   [Delete Booking Modal](#delete-booking-modal)
    -   [Visit Users Profiles](#visit-users-profiles)
    -   [Book A Class Page](#book-a-class-page)
    -   [Club News Page](#club-news-page)
    -   [News Post Page](#news-post-page)
    -   [Contact Us Page](#contact-us-page)
    -   [Messaging](#messaging)
    -   [Error pages](#error-pages)
    -   [Admin Panel](#admin-panel)
-   [Responsive design testing](#responsive-design-testing)
-   [Bugs](#bugs)

# User story testing

# Owner/Admin & Developer goals

<details>

<summary style="font-size: 20px; font-weight: bold;">Results</summary>

| Test                                                                                                                                                                                               | Expected Result                                                                 | Pass     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | -------- |
| As a developer I can select a colour scheme so that the websites colouring creates a positive user experience and also meets the stakeholders aesthetic goals.                                     | Colour scheme created in line with user story                                   | &#10004; |
| As a developer I can select the websites fonts so that I can provide a good user experience, highlighting readability and stakeholder branding goals.                                              | Fonts selected in line with user story                                          | &#10004; |
| As a developer I can construct wire-frames so that I have details of the website layout, features and style before coding begins.                                                                  | Wireframes constructed before coding began                                      | &#10004; |
| As a developer I can create an entity relationship diagram so that I can define all database entities, the information they will store and their relationship to one another.                      | ERD created detailing all models and relationships                              | &#10004; |
| As a Developer I can add styling to the website so that it is visually appealing to the user, easy to use and all content is accessible and readable.                                              | Styled to be visually appealing and has high accessibility scores site wide     | &#10004; |
| As a Developer I can create custom error templates for common errors so that the user is provided with a safe way to return to our website if an error occurs and the website maintains a good UX. | Error templates created for 400, 401, 403, 404, 500 and 503                     | &#10004; |
| As a Developer I can implement logic to limit the number of bookings a class can have so that the art class does not exceed capacity.                                                              | Logic working correctly to limit number of bookings per class to 20             | &#10004; |
| As a Developer I can add messaging to the website so that I can provide the user with feedback regarding the action they have performed.                                                           | Messaging shown for all user interaction with the website                       | &#10004; |
| As a Developer I can create a detailed readme file so that the reader can understand my development process and website functionality.                                                             | Detailed [readme](README.md) created                                            | &#10004; |
| As a Developer I can create a detailed testing file so that the reader can understand my testing process, any issues I encountered and how I fixed those issues.                                   | Detailed testing file created                                                   | &#10004; |
| As a Developer I can carry out user story testing so that I can confirm the finished project meets the user story requirements.                                                                    | Story testing completed successfully                                            | &#10004; |
| As a Developer I can carry out validation of my code so that I can ensure it complies to coding guidelines.                                                                                        | All validation carried out                                                      | &#10004; |
| As a Developer I can carry out manual site testing so that I can confirm the correct operation of the website.                                                                                     | Manual testing complete and documented                                          | &#10004; |
| As a Developer I can carry out lighthouse testing on all my webpages so that I can assess my websites performance and accessibility.                                                               | Lighthouse testing complete with excelling scores                               | &#10004; |
| As a Developer I can carry out responsive design testing so that I can ensure my website works on a variety of screen sizes, from mobile to large desktop.                                         | Responsive testing complete-no issues found                                     | &#10004; |
| As a developer I can convert uploaded images to WEBP format so that my website has faster load time.                                                                                               | Django resized library used to upload post images in webp format at 75% quality | &#10004; |
| As an Admin I can create, read, update and delete posts so that I can add and manage news post on my website.                                                                                      | Full crud functionality available from admin panel                              | &#10004; |
| As an Admin I can mark my posts as draft when creating them so that I can save a post without publishing it to the website for completion at a later date.                                         | Posts can be marked as drafts as well as archived                               | &#10004; |
| As an Admin I can approve or reject comments so that I can filter out any inappropriate comments.                                                                                                  | Comment approval or rejection fully functional                                  | &#10004; |
| As an Admin I can perform crud on user profiles, art classes and bookings so that I can manage any inappropriate content or where applicable delete harmful users profiles.                        | Admin panel provides full crud functionality for all user models                | &#10004; |

</details>

# First time visitor goals

<details>

<summary style="font-size: 20px; font-weight: bold;">Results</summary>

| Test                                                                                                                                                                | Expected Result                                                                              | Pass     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------- |
| As a User I can navigate through the website with ease understanding layout and calls to action so that I can make use of the websites various functionality.       | Easy to use responsive navbar implemented. Uniform calls to action used site wide            | &#10004; |
| As a User I can view the website on multiple devices with different screen sizes so that I can have an excellent viewing experience regardless of the device I use. | Website is fully responsive from 320px up.                                                   | &#10004; |
| As a User I can sign up and create an account so that I can login to comment on posts, like posts and make bookings.                                                | Sign in via allauth implemented as well as post commenting, liking posts and booking classes | &#10004; |
| As a User I can view a paginated list of articles in relation to club news so that I can choose one to read.                                                        | Club news implemented providing a paginated list of all club posts                           | &#10004; |
| As a User I can click on a post in the list to view so that I can view full details and approved comments on a post                                                 | Clicking any club news post will bring the user to the related news article                  | &#10004; |
| As a User I can comment on a post so that I can share my opinion with regards to the post content.                                                                  | Post commenting has been implemented                                                         | &#10004; |
| As a User I can like and unlike posts so that I can quickly express my opinion of the post content.                                                                 | Post like and unliking have been implemented                                                 | &#10004; |
| As a User I can make a booking for an art class so that I have a note of the art classes I will be attending and I reserve my place for attending the art class.    | Art class booking fully functional. Bookings can be viewed from the profile page             | &#10004; |
| As a User I can view an about us page so that I can learn all about the art club, who runs it and the classes it offers.                                            | About us implemented in line with user story                                                 | &#10004; |
| As a User I can view a home page so that I can be introduced to the club and be provided with access to booking a class or reading the club news.                   | Home page implemented in line with user story                                                | &#10004; |

</details>

# Returning visitor goals

<details>

<summary style="font-size: 20px; font-weight: bold;">Results</summary>

| Test                                                                                                                                                | Expected Result                                                                 | Pass     |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | -------- |
| As a User I can click on the art clubs social links in the footer so that I can visit the art clubs various social networks and interact with them. | All social network links work as intended                                       | &#10004; |
| As a User I can login so that I can access my account, view my bookings, comment and like posts etc.                                                | Returning user can login, book classes, comment on posts and like / unlike post | &#10004; |
| As a User I can logout so that I can no longer access my account and associated functionality.                                                      | Log out functionality implemented using allauth                                 | &#10004; |
| As a User I can view my profile page so that I can see my account profile content.                                                                  | Profile pages show all user details                                             | &#10004; |
| As a User I can edit my profile so that I can control my profile contents.                                                                          | User info and profile contents can be edited from the profile page              | &#10004; |
| As a User I can view and delete my bookings so that I can control my art class bookings.                                                            | Art classes can be viewed, updated and deleted from the profile page            | &#10004; |
| As a User I can fill out a contact form so that I can communicate with the website owner directly.                                                  | Contact form working, email will be sent to club email containing form contents | &#10004; |
| As a User I can click the username of the commenter so that I can view their profile.                                                               | Profile viewing of other peoples profiles implemented                           | &#10004; |

</details>

[Return to Table of Contents](#table-of-contents)
[Return to README.md](README.md)

# Automated testing

## Python

The [Code institutes Pep8 linter](https://pep8ci.herokuapp.com/) was used to ensure the python code conformed to Pep8 style guidelines. The results of these can be seen below.

<details>

<summary style="font-size: 20px; font-weight: bold;">About us urls</summary>

-   ![About us urls](/documentation/testing/validation/python/about-us-urls-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">About us views</summary>

-   ![About us views](/documentation/testing/validation/python/about-us-views-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Blog admin</summary>

-   ![Blog admin](/documentation/testing/validation/python/blog-admin-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Blog forms</summary>

-   ![Blog forms](/documentation/testing/validation/python/blog-forms-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Blog models</summary>

-   ![Blog models](/documentation/testing/validation/python/blog-models-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Blog urls</summary>

-   ![Blog urls](/documentation/testing/validation/python/blog-urls-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Blog views</summary>

-   ![Blog views](/documentation/testing/validation/python/blog-views-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Bookings admin</summary>

-   ![Bookings admin](/documentation/testing/validation/python/bookings-admin-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Bookings forms</summary>

-   ![Bookings forms](/documentation/testing/validation/python/bookings-forms-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Bookings models</summary>

-   ![Bookings models](/documentation/testing/validation/python/bookings-models-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Bookings urls</summary>

-   ![Bookings urls](/documentation/testing/validation/python/bookings-urls-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Bookings views</summary>

-   ![Bookings views](/documentation/testing/validation/python/bookings-views-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Contact us forms</summary>

-   ![Contact us forms](/documentation/testing/validation/python/contact-us-forms-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Contact us urls</summary>

-   ![Contact us urls](/documentation/testing/validation/python/contact-us-urls-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Contact us views</summary>

-   ![Contact us views](/documentation/testing/validation/python/contact-us-views-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Home urls</summary>

-   ![Home urls](/documentation/testing/validation/python/home-urls-pep8ci.png)
</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Home views</summary>

-   ![Home views](/documentation/testing/validation/python/home-views-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Main settings</summary>

-   ![Main settings](/documentation/testing/validation/python/main-settings-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Main urls</summary>

-   ![Main urls](/documentation/testing/validation/python/main-urls-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Profiles admin</summary>

-   ![Profiles admin](/documentation/testing/validation/python/profiles-admin-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Profiles forms</summary>

-   ![Profiles forms](/documentation/testing/validation/python/profiles-forms-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Profiles models</summary>

-   ![Profiles models](/documentation/testing/validation/python/profiles-models-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Profiles urls</summary>

-   ![Profiles urls](/documentation/testing/validation/python/profiles-urls-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Profiles views</summary>

-   ![Profiles views](/documentation/testing/validation/python/profiles-views-pep8ci.png)

</details>

## HTML

The automated testing of this projects HTML code was carried out using [Validator w3](https://validator.w3.org/nu/), the results are shown below,

<details>

<summary style="font-size: 20px; font-weight: bold;">Results</summary>

| Page                                                                                                                                                           | Pass     | Note  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ----- |
| [Index](https://validator.w3.org/nu/?doc=https%3A%2F%2Fhappy-little-artists-f3eca52b3ca8.herokuapp.com%2F)                                                     | &#10004; |       |
| [About_us](https://validator.w3.org/nu/?doc=https%3A%2F%2Fhappy-little-artists-f3eca52b3ca8.herokuapp.com%2Fabout_us%2Fabout_us%2F)                            | &#10004; |       |
| [Club_news](https://validator.w3.org/nu/?doc=https%3A%2F%2Fhappy-little-artists-f3eca52b3ca8.herokuapp.com%2Fblog%2Fclub_news%2F)                              | &#10004; |       |
| [Blog post](https://validator.w3.org/nu/?doc=https%3A%2F%2Fhappy-little-artists-f3eca52b3ca8.herokuapp.com%2Fblog%2Fclass-8-10-110124%2F)                      | &#10004; |       |
| [Login](https://validator.w3.org/nu/?doc=https%3A%2F%2Fhappy-little-artists-f3eca52b3ca8.herokuapp.com%2Faccounts%2Flogin%2F%09)                               | &#10004; |       |
| [Signup](https://validator.w3.org/nu/?doc=https%3A%2F%2Fhappy-little-artists-f3eca52b3ca8.herokuapp.com%2Faccounts%2Fsignup%2F)                                | &#10004; | Error |
| [Logout](https://validator.w3.org/nu/?doc=https%3A%2F%2Fhappy-little-artists-f3eca52b3ca8.herokuapp.com%2Faccounts%2Flogout%2F)                                | &#10004; |       |
| [Profile](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhappy-little-artists-f3eca52b3ca8.herokuapp.com%2Fprofiles%2FAmanda%2F)                | &#10004; |       |
| [Edit user info](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhappy-little-artists-f3eca52b3ca8.herokuapp.com%2Fprofiles%2Fedit_user%2F3)     | &#10004; |       |
| [Edit profile](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhappy-little-artists-f3eca52b3ca8.herokuapp.com%2Fprofiles%2Fedit_profile%2F1%2F) | &#10004; |       |
| [Create booking](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhappy-little-artists-f3eca52b3ca8.herokuapp.com%2Fbookings%2Fcreate_booking%2F) | &#10004; |       |
| [Edit booking](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhappy-little-artists-f3eca52b3ca8.herokuapp.com%2Fbookings%2Fedit_booking%2F6%2F) | &#10004; |       |
| [Contact us](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fhappy-little-artists-f3eca52b3ca8.herokuapp.com%2Fcontact_us%2Fcontact_us%2F)       | &#10004; |       |

</details>

The error which occurred on the sign up page when validating the html code has nothing to do with my code. This is caused by how crispy forms renders the signup page. It places a ul
inside a small element when rendering the password tips. I tried to combat this by viewing the source code, extracting the form that crispy forms renders and then fixing the issue by changing the small to a div. When I did this, although the form worked correctly it lost its validation. This was due to the fact that it was no longer being created based on the allauth form. Due to this and after discussion with my mentor I decided that I would leave the crispy form library code as it was and put up with the validation error as the validation functionality gained by using the allauth form to generate the sign in form outweighed it.

## CSS

The projects CSS was validated using [W3C CSS validator](https://jigsaw.w3.org/css-validator/). The projects code was input manually into the validator under the advice of my mentor. This was done as when done via a link the validator had some issues with the bootstrap code which was not my code. My css passed with no errors or warnings and the test results can be seen below.

-   ![CSS test results](/documentation/testing/validation/css/sytles-css-validation.png).

## JavaScript

The projects JavaScript was testing using [jshint](https://jshint.com/). The code passed with no warnings or error and the results can be seen below.

![JavaScript results](/documentation/testing/validation/js/script-js-validation.png)

[Return to Table of Contents](#table-of-contents)
[Return to README.md](README.md)

# Lighthouse testing

Lighthouse testing was carried out using chrome developer tools. Overall scores we excellent. One page (index page on mobile only) did suffer with low scores in the performance but that was improved by doing the following.

-   Halviing the size if the images.
-   Reducing the quality of the images used by up to 50%.
-   Compressing the images multiple times.
-   Using block tags to remove the lightbox css and related scripts from base and only using them in html files that require them.

## Mobile

<details>

<summary style="font-size: 20px; font-weight: bold;">About us</summary>

-   ![About us lighthouse](/documentation/testing/lighthouse/about-us-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Blog post</summary>

-   ![blog post lighthouse](/documentation/testing/lighthouse/blog-post-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Club news</summary>

-   ![club news lighthouse](/documentation/testing/lighthouse/club-news-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Contact us</summary>

-   ![contact us lighthouse](/documentation/testing/lighthouse/contact-us-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Create booking</summary>

-   ![create booking lighthouse](/documentation/testing/lighthouse/create-booking-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Edit booking</summary>

-   ![edit booking lighthouse](/documentation/testing/lighthouse/edit-booking-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Edit info</summary>

-   ![edit info lighthouse](/documentation/testing/lighthouse/edit-info-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Edit profile</summary>

-   ![edit profile lighthouse](/documentation/testing/lighthouse/edit-profile-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Index</summary>

-   ![index lighthouse](/documentation/testing/lighthouse/index-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Logout</summary>

-   ![logout lighthouse](/documentation/testing/lighthouse/logout-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Profile</summary>

-   ![profile lighthouse](/documentation/testing/lighthouse/profile-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Sign in</summary>

-   ![sign in lighthouse](/documentation/testing/lighthouse/signin-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Sign up</summary>

-   ![ sign up lighthouse](/documentation/testing/lighthouse/signup-mobile-lighthouse.png)

</details>

</details>

## Desktop

<details>

<summary style="font-size: 20px; font-weight: bold;">About us</summary>

-   ![About us lighthouse](/documentation/testing/lighthouse/about-us-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Blog post</summary>

-   ![blog post lighthouse](/documentation/testing/lighthouse/blog-post-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Club news</summary>

-   ![club news lighthouse](/documentation/testing/lighthouse/club-news-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Contact us</summary>

-   ![contact us lighthouse](/documentation/testing/lighthouse/contact-us-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Create booking</summary>

-   ![create booking lighthouse](/documentation/testing/lighthouse/create-booking-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Edit booking</summary>

-   ![edit booking lighthouse](/documentation/testing/lighthouse/edit-booking-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Edit info</summary>

-   ![edit info lighthouse](/documentation/testing/lighthouse/edit-info-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Edit profile</summary>

-   ![edit profile lighthouse](/documentation/testing/lighthouse/edit-profile-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Index</summary>

-   ![index lighthouse](/documentation/testing/lighthouse/index-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Logout</summary>

-   ![logout lighthouse](/documentation/testing/lighthouse/logout-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Profile</summary>

-   ![profile lighthouse](/documentation/testing/lighthouse/profile-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Sign in</summary>

-   ![sign in lighthouse](/documentation/testing/lighthouse/signin-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Sign up</summary>

-   ![ sign up lighthouse](/documentation/testing/lighthouse/signup-desktop-lighthouse.png)

</details>

# Manual testing

The tests for this app listed below were conducted to ensure it correct operation. All tests passed successfully

## Header brand

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Navigation

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Footer

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Home Page

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## About Us Page

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Sign up Page

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Sign in Page

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Log out Page

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Profile Page

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Empty Profile

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Edit Info Page

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Edit Profile Page

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Edit Booking Page

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Delete Booking Modal

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Visit Users Profiles

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Book A Class Page

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Club News Page

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## News Post Page

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Contact Us Page

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Messaging

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Error pages

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

## Admin Panel

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

[Return to Table of Contents](#table-of-contents)
[Return to README.md](README.md)

# Responsive design testing

The Responsive design testing was carried out during and after the development of the website. Firefox's development tools were used to ensure that all webpages not only looked good at the bootstrap breakpoints, but at all points in between. This was accomplished by altering the screen width from 320px up and and making changes to the code using bootstraps grid system. In cases where the grid system could not achieve the desired sizing or layout custom media queries were added. After the website was completed it was tested on my Huawei P30 pro and all pages passed responsive testing.

[Return to Table of Contents](#table-of-contents)
[Return to README.md](README.md)

# Bugs

During testing some bugs were found and fixed, these were,

### Bug 1

<details>

<summary style="font-size: 20px; font-weight: bold;"></summary>

| Test | Expected Result | Pass     |
| ---- | --------------- | -------- |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |
|      |                 | &#10004; |

</details>

[Return to Table of Contents](#table-of-contents)
[Return to README.md](README.md)
