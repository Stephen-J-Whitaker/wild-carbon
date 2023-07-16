# **Wild Carbon**
[‘Wild Carbon’]( https://wild-carbon-803b1e2f6e91.herokuapp.com/) is a website (hosted on [Heroku](https://www.heroku.com/) and implemented with the aid of the Python Django framework) that’s for people who want to offset their carbon footprint and care about the environment.

Wild Carbon offers a service where users of the website can commission trees to be grown and planted on their behalf at Wild Carbon’s site in the west of Ireland. Once planted, the trees are allowed to grow in the protected, newly rewilded, site for the duration of the trees’ lives, gradually sequestering carbon for the people who commissioned them.

The company isn’t only about providing a carbon sequestration service,
. It’s also about rewilding, the return of areas that have been cultivated, perhaps for many years, to a wild state. This involves the planting of the commissioned native trees along with other flora that would have naturally inhabited the site. In turn, this replanting of the site encourages the return of the native fauna.

Sequestering carbon for the Wild Carbon customers whilst increasing the natural biodiversity of areas of land is the mission of Wild Carbon.

- [Link to live ‘Wild Carbon’ website]( https://wild-carbon-803b1e2f6e91.herokuapp.com/)


![Responsive mockup]( docs/images/readme_responsive_mockup.jpg)

## **Contents**

1 [Project Initiation](#1-project-initiation)

2 [Wild Carbon development](#2-wild-carbon-development)

3 [Features](#3-features)

4 [Testing](#4-testing)

5 [Project Sign Off](#5-project-sign-off)

6 [Releases](#6-releases)

7 [Deployment](#7-deployment)

8 [Technologies Used](#8-technologies-used)

9 [Credits](#9-credits)

10 [Acknowledgements](#10-acknowledgements)


## **1. Project Initiation**

- ## Agile

    - ### Epics, User Stories and Tasks

        An agile approach was taken to the planning and implementation of the project. Epics were identified for the project from the basic requirements of an ecommerce store that would be selling the service of growing and planting trees to sequester carbon. As would be true of many e-commerce stores, these epics were the website, the shop functionality of the website and fulfillment management for orders placed.

        The epics were then refined into user stories, the user stories associated tasks and the acceptance criteria for the features developed to satisfy the user stories.

        As the project was planned, it was ensured that there was no functionality duplicated across features and that code could be reused wherever possible.

        As each user story was planned, new acceptance criteria were added to features as required for the user story in question to be satisfied. User stories were analysed in order of priority with functionality of later planned user stories building on the functionality of previously planned ones. This meant that the features functions that were worked on for later developed user stories were dependent on the earlier user stories being completed.

	    A stack of user stories in a kanban board was used to manage the order in which user stories were worked and ensure they were worked on in the correct order considering their priorities and interdependencies.  
        
        All feature acceptance criteria from all user stories were consolidated onto a single list from which a test plan could be produced.

        Note: During the planning and refinement phase, some features were combined with others and the feature ids of the features no longer required were removed from use, hence there are gaps in the feature id numbering system. No feature that is a requirement of the system has been omitted from the documentation.

        -   [Epics and User Stories](docs/pdfs/readme_epics.pdf)
        -   [Epic specifications](docs/pdfs/readme_epic_specifications.pdf)
        -   [Epic / User Story Acceptance Criteria](docs/pdfs/readme_epic_acceptance_criteria.pdf)
        -   [Consolidated Feature Acceptance Criteria](docs/pdfs/readme_feature_acceptance_criteria.pdf)

    - ### MoSCoW

        Once the design planning had taken place, the number of story points allocated to each user story was decided by considering the user storys’ tasks complexity and size. 

	    User stories were prioritised to ensure, firstly, the earliest possible return on investment for Wild Carbon followed by maximizing that return and lastly streamlining the fulfillment processes. In terms of the development of the software, this meant that the e-commerce part of the store being functional was the highest priority, followed by marketing for the company’s service to increase customer reach hence increasing the probability of making sales and, lastly, front end custom fulfillment functionality. Fulfillment functionality could easily be worked around in the standard Django admin pages should there be insufficient time to complete all fulfillment epic user stories. 

	    Using the MoSCoW technique all user stories were given a priority of 'must have', 'should have' or 'could have'. There were no ‘won't have’ user stories.

        -   [Iteration 1 MoSCoW Analysis](docs/pdfs/readme_moscow_analysis.pdf)

    - ### Agile tools

        Tools in GitHub were used to manage the project development phase. The user stories were entered as issues along with their associated tasks and acceptance criteria as well as the acceptance criteria for the features developed to satisfy the user stories.

        The user stories were given labels that indicated the epic they belonged to, their MoSCoW rating and the number of modified Fibonacci scaled story points that they had been allocated. 

        Initially the user stories (issues) were placed on the product backlog (implemented using a milestone) and were then moved onto the project Iteration 1 milestone when it was decided that they would be worked on during that iteration. The iteration was a 4 week period. 

        During the iteration, the user stories were managed in a GitHub project on a kanban board. As planned, in the order of priority, the user stories were moved from the 'ToDo' to 'In Progress' and, once complete, to 'Done. 

        Portion of Kanban

        ![Kanban](docs/images/readme_kanban.jpg)

    - ### User Story / Task Prioritisation

        The order that the user stories were worked on was dependent on the MoSCoW priority along with the dependencies of each of the user stories. 

        The features and functionality of user stories moved into the ‘in progress’ column were often dependent on the completion of user stories worked on before them. These dependencies were ascertained during the project initiation/planning stage and the additional acceptance criteria required for each feature for the user story in question were appended to those defined for the user stories developed beforehand. By appending all new requirements to the bottom of the list of previous feature acceptance criteria, a full set of feature acceptance criteria was developed. 

        Example User Story

        ![User Story](docs/images/readme_user_story.jpg)

    - ### Acceptance Tests

        From this full feature set list and those features acceptance criteria, manual testing procedures were developed that would ascertain if the acceptance criteria for the user stories, all the features and therefore the project as a whole had been satisfied. 

        When it was believed that a user story development had been completed, the test script compiled to that point was run through to ensure that both the new set of tests for the most recent user story and those defined beforehand, for previous user stories, all passed as all the previous functionality was required for the new user story and any other user story that uses the feature the tests relate to.

## **2. Wild Carbon Development**

-   ## Business Model 

        Wild Carbon has a business to customer business model, where using a single payment model, they offer the service of growing and planting trees to order on the customers behalf. The planting of the trees is to sequester carbon from the atmosphere for the site user whilst rewilding and protecting the site on which the trees are planted.
        
        Made apparent by an ever increasing number of extreme weather events there is a greater awareness than ever of the climate shift that is taking place and the impact that most people’s lifestyles have on our environment. There has never been a better opportunity for this business to succeed in ‘making a difference’.

    -   ### Customers

        Wild Carbons customers are conscious of the impact that their lifestyle has on the environment both in terms of the carbon dioxide their lifestyle adds to the atmosphere but also the cultivation of the landscape for the production of food.

        The Wild Carbon service will appeal most to those who feel that there is an urgent need to try to restore our environment both in terms of the climate and areas of countryside. These people will often have the greatest vested interest in the future such as younger people and parents who care about the environment’s future for their children but it will also appeal to anyone who is conscious of the impact their life has had on the environment and would like to reverse this impact.

        The site would also appeal to residents of Ireland who are aware of the deforested nature of the country and would like to see more of Ireland returned to its natural state.

    -   ### Competition

        There is competition in the field of carbon sequestration through the planting of trees but very little to none, especially in Ireland, that offer it whilst focusing on rewilding the site as part of the process.

-   ## Marketing 
    The marketing strategy is currently fourfold:

    -   ### Search engine optimisation:

        Indexing of the site
        Optimising the website for search engines included the production of a robots.txt and sitemap.xml so that the site can be indexed appropriately.
        
        -   [robots.txt](https://wild-carbon-803b1e2f6e91.herokuapp.com/robots.txt)
        
        -   [The robots.txt file can be found here](https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/templates/robots.txt)
        
        -   [sitemap.xml]( https://wild-carbon-803b1e2f6e91.herokuapp.com/sitemap.xml)
        
        -   [The sitemap.xml file can be found here](https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/templates/sitemap.xml)
        
    -   ### Keywords
    
        Long and short tail keywords for Wild Carbon were researched on google and in [wordtracker.com]( https://www.wordtracker.com). These keywords have been included in the headers and in the content of the website, in the landing page content in particular. The success or failure of the keywords can be monitored in Google Analytics and, as necessary, the keywords can be left in place, altered or replaced.
    
        -   The keywords selected are:
        
            -   improve biodiversity
        
            -   carbon footprint

            -   carbon sequestration

            -   carbon offset

            -   rewild Ireland

            -   carbon neutral

            -   carbon neutrality

            -   offset my carbon footprint in Ireland

            -   wild carbon

            -   plant trees

            -   rewilding

            -   carbon calculator

            -   how do I sequester my life’s carbon footprint

    -   ### Other optimisation

        The site contains links to external sites with credibility and a high search engine ranking to help boost Wild Carbon’s own search engine ranking.
        File names and alt text are relevant. By providing useful links to credible external sites that will be of interest to the users of the site, search engine ranking will be improved.

        Internal URLs are relevant where possible. [for example: https://wild-carbon-803b1e2f6e91.herokuapp.com/locations/carbon_capture/]( https://wild-carbon-803b1e2f6e91.herokuapp.com/locations/carbon_capture/).

    -   ### Coming soon
    
        There is a ‘coming soon’ section on the landing page of the website detailing a future opportunity of sponsoring the preservation of areas of blanket bog to ensure the carbon locked within them remains there. This essentially offsets the customers carbon in a very cost effective way. 

        It is hoped that Customers will be encouraged by the coming soon section to sign up for the newsletter and return to the site on notification of the new service that they may be happier to avail of than the current tree commissioning service in place.

    -   ### Newsletter
    
        There is newsletter signup functionality incorporated into the landing page. 

        People who sign up for the newsletter will receive periodic information on subjects that are likely to be of interest to them. Subjects of interest would include, but are not limited to, useful hints on how to improve their carbon footprint going forward, any new initiatives that Wild Carbon are developing and events that Wild Carbon will be attending, (in case potential customers would like to meet staff members in person to help them feel confident in company and in turn its service).

    -   ### Social media

        Being a small startup company with no marketing budget currently and given the age group that the company’s rewilding carbon sequestration service will appeal to most, the company will be making the use of social media. 

        A Facebook business page has been set up that is linked to via a button in the footer of the website.

        -   [Wild Carbon’s Facebook business page]( https://www.facebook.com/wild.carbon.sequestration)
        
        ![ Wild Carbon’s Facebook business page screenshot]()

 





- ### **Wild Carbon Style Development**

  - ### **Website Interface Development**

    - ### Interface Mockups
        
        The interface was developed to incorporate all of the features necessary to satisfy the user stories into an easy to navigate, intuitive and aesthetically pleasing design.
	
    -   [Mobile Interface Mockups](docs/pdfs/readme_mobile_interface_mockups.pdf)

    -   [Tablet Interface Mockups](docs/pdfs/readme_tablet_interface_mockups.pdf)

    -   [Desktop Interface Mockups](docs/pdfs/readme_desktop_interface_mockups.pdf)

    -   ### Interface Design

        The style of the interface was designed to be as conventional as possible to ensure that a user can easily identify the functions they require and that using these functions is intuitive.

        Imagery is used to increase the interest of the site and content is placed into inner containers with a different background colour the body of the site to break up white space and make the site generally more aesthetically pleasing.

    -	### Interface Layout

        The layout was inspired by other e-commerce websites to be familiar to the user, ensuring ease of use. It is consistent across pages and easy to navigate. 

        -   Header and Footer
        
            The header contains the main navigation menus for the site and is at the top of all pages for continuity and ease of navigation.

            The header is responsive and the main navigation is activated by a toggle button on smaller devices.

            The footer is at the bottom of the page and, if the content of the page is not high enough to fill the entire view port on its own, the main content expands to ensure that the footer is at the bottom of the page view port, again for aesthetics.

        -   Main Content

            The main content is as vertically long as necessary to contain the content so that only the window scroll bar is necessary, except in the case of some tables and the privacy statement. 

            In the case of some tabulated data and the privacy statement the containers become scrollable if they overflow their containers.

        -   Responsiveness
    
            The interface was designed using a mobile first approach.
            
            On large devices the width of the interface is restricted to the middle section of the screen so as not to become too large to be easily read and access functions.

            The site is responsive and elements resize and in the case of the navigation menu change arrangement, as necessary to fit on the screen in use and retain usability.

            With the exception of the contact email address (which resizes relative to the width of the view port), words and content, such as the order number, that do not fit on a single line are broken and wrap to the next line. 

    -	### Typography

        A limited set of fonts were selected for the typography of the site. This helps to ensure that the site retains a consistent, coherent feel. 

        Khand and Lato are imported from [google fonts]( https://fonts.google.com/). They are easy to read at all screen sizes and are relatively narrow ensuring that characters don’t take up excessive space on small, mobile devices.
	
        -   Brand and Headers

            The brand name ‘Wild Carbon’ and the headers are the google font ‘Khand’. The use of this font for the brand and headers helps to establish a brand identity that can become recognisable and contributes to the coherence of the site. It is easy to read at all sizes required for the site.

        -   Site Text

            Google font Lato was selected as the primary font for all text on the site that isn’t the brand name or a header. It resizes well and is easy to read at all sizes required for the site.

    -   ### Colour Schemes

        The colour scheme of the interface was chosen to be calming, natural shades of green.

        - Interface

            Various shades of green with varying transparencies were selected for the interface in conjunction with the paler harmonious colours of the text to create sufficient contrast between the background and the text ensuring excellent accessibility. 

        - Text

            For coherence and aesthetics, the colour of the text is either a very light shade of green or white. The depth of the shade was in part determined by the necessity for contrast between the text and the backgrounds for accessibility. 

            The colour of the text was chosen for coherence with the background to help ensure a positive user experience when using the site.

        -   Shading

            All colours on the site are ‘flat’ except for any drop shadows used. Drop shadows are only used on hovering over an ‘image link’. Image links are used on the landing page to navigate to the ‘carbon capture’, ‘how it works’ and ‘about us’ pages and on the ‘carbon capture’ and ‘plant admin’ page to navigate to the ‘plant detail’ and ‘edit plant’ pages, respectively. 

    -   ### Icons, Graphics and Images

        -   Favicon

            The site favicon is an image of a leaf with waves of blue, representing air, aiming at the leaf. The background of the leaf is transparent to help the favicon appear embedded into the browser tab.

	        Selected to represent the sequestration process of leaves taking in air in order to extract carbon dioxide, the favicon is relevant to the Wild Carbon service and helps increase brand identity as well as aiding a user in identifying the tab containing the site. Its also intended to act as a subconscious reminder of the importance of the service and lead to additional tree planting commissions.


        -	Icons

	        Icons are used in various places in the site to add interest. All of the icons were either sourced from [Font Awesome]( https://fontawesome.com/) as SVG files or are linked in the site and served directly by Font Awesome.

        -	Graphics

            An SVG graphic of a seedling, sourced from Font Awesome, is used on the main page title on the landing page. It is relevant to the service provided by the site and is used to add interest.

        -	Images

            Various images are used on the site to add interest.

            The landing page contains a large image of a glade that represents the vista of a site once it has been rewilded by the Wild Carbon service. The shades of green match well with the interface and is intended to be a pleasant, relevant and in the case of return visits, familiar, welcome to the site.

            The same glade image is used a background for the privacy statement and contact us modals.

            The images used on the landing page as navigation links are relevant to the destination of the link.

            The carbon capture image link is an image of the Wild Carbon site location.

            The About us image link is a picture of a person carefully holding a seedling to represent the work that is done by the company and the care that the company applies to each plant.

            The How it works image link is an image of a tree with molecules of co2 and o2 floating around it representing the carbon sequestration process.

            All images are responsive to changes in screen size and are configured ensure the container is filled.

            Images can be uploaded against the plant products. The image should be relevant to the product that it’s used to represent.

            All images are currently an artists representation of the tree product it is uploaded against. The image shows some of the plants distinguishing features and an image of a person to indicate scale and the final potential height of the tree.

            Should no image be uploaded against a plant product, a generic ‘no image’ image is shown though this should only be used as a placeholder and it is preferred that a unique, relevant image be uploaded against each product.

    -   ### Interface styling and User Feedback:

        Features style and user feedback is consistent across the site. In all cases a successful click is indicated by the requested action taking place and any action that is related to database data manipulation is signaled by a Bootstrap toast message at the top of the screen. The toast message notifies the user of the outcome of the action. The message categories are success (background green), failure/error(background red) and information(background blue).

        -   Logos

            The logos on the site are all the same colour for consistency.

            On hover the logos obtains a rectangular green backdrop that is a deeper shade of the logos normal backdrop. This helps to identify the logo as a clickable link.

            Clicking a logo takes a user to the top of the landing page if they are on the landing page or back to the landing page if they are elsewhere on the site.

        -   Navigation

            -   Header Navigation
            
                Navigation menus are consistent across all pages of the site for consistency to help ensure using the site is a positive user experience. Having the navigation menus on all pages of the site makes navigating the site to explore and find particular features easier.

                There is a icon representing a person’s torso in the header that when clicked activates a dropdown that displays account related links.

                The account links change a lighter colour on hover to identify them as a clickable link. 

                Links relevant to the login state of the user are displayed.

                The account menu and icon are the same across all screen sizes

                The header also contains an image of a basket that when clicked navigates to the basket page of the site.

                Below the basket icon is the total value of the items currently in the basket.

                The basket icon is the same across all screen sizes.

                -   Main navigation

                    The links of the main navigation bar are in a row on larger screens. The are styled with an underline and turn a lighter colour on hover to indicate that they are clickable.

                    When logged in as a superuser or staff member there is an additional ‘Administration’ dropdown menu that contains links to administration functions of the site

                -   Navigation on mobile devices

                    The navigation becomes a drop down that is displayed when a toggle button is clicked. The styles of the links in the drop down are the same as when the navigation is viewed on larger screens and obtain an underline on hover to indicate that they are clickable.

                    The toggle button is styled like all other buttons on the site, having rounded corners and being the same colour as the other buttons.


            -   Image Navigation
            
                Image navigation is where an image can be clicked and another page of the site will be navigated to. There are two types of image navigation in the site.

                On the landing page there is image navigation to the ‘carbon capture’, ‘how it works’ and ‘about us’ pages. The images have rounded corners to help distinguish them from content and obtain a dark green drop shadow on hover to identify them as clickable links. 

                The other style of image navigation is on the plant products pages. In the ‘carbon capture’ page and the ‘plant admin’ page the plant product containers have an image in them as part of the description of the plant. 

                The container for the plant information obtains a light green drop shadow on hover in contrast with the background of the content container behind it. The drop shadow to identifies them as clickable links. 

        -   Buttons and links

            Buttons are how actions on the site are triggered and how links to other pages are represented on the site when not in the header, footer or a table. 

            In the case of tables, to aid the responsiveness of the site by making the link more compact than a button would be, the links are styled like links in the navigation. This is necessary due to the high density of the information to be conveyed within the tables.

            Buttons can be found in two colour on the site. With the exception of the buttons on account related pages, ‘Useful Links’ on the ‘how it works’ page and the negative symbol button on the quantity change feature, all buttons are a grey/green that becomes a lighter shade on hover to indicate that its a clickable entity. The text within is a very deep green shade.

            To help separate account functions of the site from general functions of the site, the buttons on the account related pages are a deep green that becomes deeper on hover. The text is a very light yellow/green to ensure a sufficient contrast ratio for accessibility.

            ‘Useful Links’ on the how it works page are styled in the same way as account function buttons to distinguish them from buttons that carry out internal site functions or that act as internal site page links.

            The choice of button colours helps to distinguish the buttons from the other features of any given.

            The negative symbol button in the quantity selection features of the site is to easily distinguish them from the negative symbol button. 

            An exception to these above button styles is that the remove button on the basket page has red text as a warning to the user.

        -   Forms

            All forms on the site are styled with Django Python package Crispy Forms. The form inputs have a very pale green background for aesthetics.

            The form inputs change to a lighter shade of green when in focus or active to indicate that they are the selected input. The colours of the input fields have been selected for colour contrast between text and background and hence accessibility.

        -   Content

            Containers for content on the site can be found in two styles.

            Title containers that are to be found on pages that are not administration related do not have margins and are fully responsive. The background image fully covers the container.

            Content is inside a responsive green container that has a margin and sharp corners to help identify it as an area of content and distinguish it from image navigation.

            Text is centered except where it is in the form of a list or table in which case where it is left or right justified.

            All tables and their text is in the main site text colour and the content is responsive.



## **3. Features**





-   ### **Potential future features**


## **4. Testing**
-   **Code Validation**

-   **Functionality Test Results**

    **Other Testing**

-   **Bugs Found and Resolved or Current**

## **5. Project Sign Off**

## **6. Releases**

## **7. Deployment**


## Forking the Repository

## Clone the Repository

## **8. Technologies Used**

- [Python](https://www.python.org/)

-   Django

-   HTML

-   CSS

-   JavaScript

-   ElephantSQL : Hosts a postgres database for the project

-   Amazon AWS S3 Bucket : Cloud storage for static and media files

-   Bootstrap : Used to implement the responsive navigation bar, add styles using their preconfigured classes and a dependency of some Django packages

-   Google Fonts : Used for fonts Khand’ and 'Lato'

-   Code institute student template for GitPod and Codeanywhere: Used to install the necessary IDE tools and set up GitPod, Codeanywhere and GitHub Codespaces as required

-   The W3C Markup Validation Service : Used to validate the website HTML

-   The W3C CSS Validation Service - Jigsaw : Used to validate the website CSS

-   JSHint, a JavaScript Code Quality Tool (linter): Used to validate and check the styling of the website JavaScript

-   Favicon.io : Used to create the favicon for the site

-   JQuery : Used for its implementation of Ajax

-   Font Awesome : Used to source icon svg files and serve icons as referenced in the code

-   Ajax : Used to validate data entered by the user

-   pgAdmin : Used to access the postgres database and verify create, read, update and delete was happening as required

-   [Corel Draw](https://www.coreldraw.com/en/) : Used for developing the mockups for the app

-   [Microsoft Excel](https://www.microsoft.com/en-ie/microsoft-365/excel) : Used for documenting features and recording test results

-   [Microsoft Visio](https://www.microsoft.com/en-ie/microsoft-365/visio/flowchart-software) : Used for producing Epics, User Stories and the database entity relationship diagram.

-   [Chrome](https://www.google.com/intl/en_ie/chrome/) : Used for research, development and testing (including DevTools and Lighthouse test suite)

-   [Safari](https://www.apple.com/safari/) : Used for testing

-   [Opera](https://www.opera.com/) : Used for testing

-   [Edge](https://www.microsoft.com/en-us/edge) : Used for testing

-   [Firefox](https://www.mozilla.org/en-US/firefox/new/) : Used for testing

-   [Notepad++](https://notepad-plus-plus.org/downloads/) : Used for text file editing

-   [GitPod](https://www.gitpod.io/) : Used for product development and testing

-   [GitHub](https://github.com/) : Used for accessing committed code repositories and produce development and testing in its Codespaces IDE

-   [Git](https://git-scm.com/): Used for code version control

-   [Code Institute Python Linter](https://pep8ci.herokuapp.com/#): Used to validate and check the styling of the Python code

-   Windows 10 snipping tool for creating screen grabbed jpeg files for the readme

-   [TinyJPG](https://tinyjpg.com/): compression of jpg files

-   [Cloud Convert](https://cloudconvert.com/): For conversion of JPEG to WEBP format

-   [Stripe](https://stripe.com/ie): For ecommerce payment implementation

-   [MailChimp](https://mailchimp.com/): Used to handle newletter signup

-   [AmIResponsive](https://ui.dev/amiresponsive): Used to produce the mock-up at the top of this readme

## **9. Credits**

-   ### **Code**

    -  All code and text content was written by the author, Stephen Whitaker, unless explicitly stated within the code or as described below.

    -   Code and models to implement the e-commerce store functionality for Wild Carbon including products, basket, and checkout handling was adapted from the Boutique Ado walkthrough project provided by [Code Institute](http://www.codeinstitute.net/). The Boutique Ado walkthrough also included instructions on sending of emails, integration with Amazon S3 Bucket for serving static and media files and the [Stripe]( https://stripe.com/ie) payment system and these instructions were followed during implementation of the Wild Carbon project. The code sourced from or adapted from the Boutique Ado project is referenced in the Wild Carbon project code at the locations where the Boutique Ado code is in use.

    -	[Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) was used for the creation of the responsive navigation bar, toasts and some styles throughout the template code were implemented using Bootstraps css classes.

    -	Code to show success messages on successful deletion was obtained from stack exchange at the following link : https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown. The code can be found in views.py of the plants app.

    -	Settings for the configuration of an ElephantSQL database were provided by Code Institute. The code is in [Settings.py](https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/wild_carbon/settings.py) for the wild_carbon project.

    -	Settings required to configure allauth were provided by Code Institute. The code is in [Settings.py](https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/wild_carbon/settings.py) for the wild_carbon project and [urls.py](https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/wild_carbon/urls.py)

    -	Code to use ajax to send and receive data to and from a Django view was adapted from code at the following link : https://www.geeksforgeeks.org/handling-ajax-request-in-django/. The code can be found in [views.py]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/plants/views.py) and [add_edit_plant.js]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/plants/static/plants/js/add_edit_plant.js) in the plants app

    -	Code used to reduce multiple white spaces in a string to single spaces was taken from the following site: https://www.tutorialrepublic.com/faq/how-to-replace-multiple-spaces-with-single-space-in-javascript.php. The code can be found in [add_edit_plant.js]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/plants/static/plants/js/add_edit_plant.js) in the plants app

    -   The code to serve the sitemap.xml and robots.txt were taken from the following tutorial https://ngangasn.com/sitemap-robot-txt-django/?utm_content=cmp-true . The code can be found in the [urls.py]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/wild_carbon/urls.py) of the Wild Carbon project folder

    -   The [sitemap.xml]( https://wild-carbon-803b1e2f6e91.herokuapp.com/sitemap.xml) was generated at https://www.xml-sitemaps.com/

    -   Code to integrate with MailChimp for newsletter signup handling was sourced at [MailChimp]( https://mailchimp.com/) and is imported in [index.html]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/home/templates/home/index.html)

    -   Code to implement the creation of many to many relationships between the location and plants available at that location was sourced at https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024. The code can be found in [forms.py](https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/locations/forms.py) and [views.py](https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/locations/views.py) of the locations app.
    
    -   Code to confirm if a user trying to access a view is a superuser was sourced at https://stackoverflow.com/questions/67351312/django-check-if-superuser-in-class-based-view. The code can be found in [mixins.py]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/wild_carbon/mixins.py) in the Wild Carbon project folder

    -   Code to confirm deletion of a plant was sourced from the [Music Aid project]( https://github.com/Stephen-J-Whitaker/music-aid). The code can be found in the DeletePlant class in [views.py]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/plants/views.py) in the plants app

    -   Code to validate whether a plant common name as entered by a user in the add and edit plant views was unique in the database was sourced from the [Music Aid project]( https://github.com/Stephen-J-Whitaker/music-aid). The code can be found in the common_name_validate function in [views.py]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/plants/views.py) and [add_edit_plant.js]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/plants/static/plants/js/add_edit_plant.js) in the plants app


-   ### **Content**

    -   The privacy policy for the site was generated at https://www.privacypolicygenerator.info/ and can be found in [privacy_policy.html]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/templates/includes/privacy_policy.html)

    -   The [Facebook business page](https://www.facebook.com/wild.carbon.sequestration) for Wild Carbon was generated and is hosted by [Facebook]( https://www.facebook.com/)

    -   A link to [carbonfootrint.com’s]( https://www.carbonfootprint.com/calculator.aspx) carbon footprint calculator was used in the [Useful Links]( https://wild-carbon-803b1e2f6e91.herokuapp.com/how_it_works/) section of the Wild Carbon website

    -   A link to [rewildingeurope.com’s]( https://rewildingeurope.com/what-is-rewilding/) description of rewilding was used in the [Useful Links]( https://wild-carbon-803b1e2f6e91.herokuapp.com/how_it_works/) section of the Wild Carbon website

    -   A link to [treecouncil.ie’s]( https://www.treecouncil.ie/carbon-footprint) carbon footprint facts was used in the [Useful Links]( https://wild-carbon-803b1e2f6e91.herokuapp.com/how_it_works/) section of the Wild Carbon website

    -   Plant information was sourced at the [RHS]( https://www.rhs.org.uk/) website

    -   [WordTracker](https://www.wordtracker.com/) was used for keyword research for search engine optimisation

    -   [FontAwesome]( https://fontawesome.com/) used to source icon SVG files and other icons as served by them. The icons are referenced in the code

-   ### **Media**

    -   The main heading image of a [glade]( https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/static/images/base_home_index_glade.webp) was sourced at https://www.pexels.com/photo/green-forest-under-white-sky-during-daytime-165537/

    -   The [carbon capture location]( https://raw.githubusercontent.com/Stephen-J-Whitaker/wild-carbon/main/static/images/carbon_capture_location.webp) image was soured at https://iowalandcompany.com/jones-county-iowa-80-acres-for-sale/

    -   The image of [a person holding a seedling]( https://raw.githubusercontent.com/Stephen-J-Whitaker/wild-carbon/main/home/static/home/images/home_about_us_plug_plant.webp) was sourced at https://github.com/Stephen-J-Whitaker/wild-carbon/blob/main/home/static/home/images/home_about_us_plug_plant.webp

    -   The image of a [tree with CO2 and O2 molecules around it]( https://raw.githubusercontent.com/Stephen-J-Whitaker/wild-carbon/main/home/static/home/images/home_how_it_works.webp) was sourced at https://ecotree.green/en/how-much-co2-does-a-tree-absorb

    -   The plant images used for the plant products were sourced at [treecouncil.ie](https://www.treecouncil.ie/native-irish-trees)

## **10. Acknowledgements**

-   A special thank you to my mentor Marcel Mulders

-   Thank you to all those who were kind enough to test the website and provide feedback
