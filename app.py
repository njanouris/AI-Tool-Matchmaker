/*Global color variables*/
:root {
    --background-color: #616569;
    --text-color-light-green: #E8F5E9;
    --text-color-white: #FFFFFF;
    --accent-color-neon-green: #39FF88;
    --accent-color-blue: #00B4D8;
    --accent-color-dark-blue: #003366;
    --header-color-dark-blue: #0B1E4B;
    --accent-color-yellow: #D9A441;
    --navbar-color: #0A1410;
    --border-color: #39FF88;
    --border-color-backup: #6B4423;
    --cream-color: #F5EFE0;
    --brown-color: #5C4033;
}

/*Sets the background color of the whole website*/
.stApp {
    background-color: var(--background-color);
}

/*Keeps section titles from hiding under the nav bar when a nav link jumps to them*/
.stApp h1,
.stApp h2,
.stApp h3,
#top {
    scroll-margin-top: 100px;
}

/*Helps to contain the main part/title of the website */
.top-text {
    border: 5px dashed var(--accent-color-neon-green);
    border-radius: 10px;
    background-color: var(--header-color-dark-blue);
    color: var(--text-color-white);
    padding: 20px;
    text-align: center;
    margin-top: 60px;
    margin-bottom: 40px;
}

.top-text h1 {
    color: var(--accent-color-neon-green);
}

/*Short yellow line that separates the title and the tagline*/
[data-testid="stMarkdownContainer"] hr.title-divider {
    width: 80px;
    border: none;
    border-top: 4px solid var(--accent-color-yellow);
    margin: 12px auto;
}

/*Navigation Bar that is at the top of the website*/
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    z-index: 999999;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 40px;
    background:
        linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.45)),
        url("https://images.unsplash.com/photo-1570454618940-165d5cc494f3?w=1600&q=60") var(--border-color-backup);
    background-size: cover;
    background-position: center;
    border-bottom: 5px solid var(--cream-color);
}

/*VipervisionAI name on the far left of the nav bar*/
.nav-logo {
    color: var(--accent-color-neon-green);
    font-size: 1.5rem;
    font-weight: bold;
}

/*Groups the links together on the right side of the nav bar*/
.nav-links {
    display: flex;
    gap: 10px;
    margin-left: auto;
}

.navbar a {
    color: var(--text-color-white);
    text-decoration: none;
    font-weight: bold;
    padding: 10px 20px;
    border-radius: 6px;
}

.navbar a:hover {
    background-color: var(--accent-color-neon-green);
    color: var(--navbar-color);
}

/*Horizontal line between the header box and the questions*/
[data-testid="stMarkdownContainer"] hr.section-divider {
    border: none;
    border-top: 4px solid var(--accent-color-dark-blue);
    margin: 0 0 40px 0;
}

/*Cards that hold each question*/
div[class*="st-key-question_card"] {
    background-color: var(--cream-color);
    border: 3px dashed var(--brown-color);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
}

/*Dark text inside the cards*/
div[class*="st-key-question_card"] p {
    color: var(--navbar-color);
}

/*Question titles: centered, bold, and underlined*/
div[class*="st-key-question_card"] [data-testid="stMarkdownContainer"] p {
    text-align: center;
    font-size: 1.1rem;
    text-decoration: underline;
    text-underline-offset: 5px;
    margin-bottom: 15px;
}

/*Dropdown boxes in brown to match the dashed border*/
div[class*="st-key-question_card"] div[data-baseweb="select"] > div {
    background-color: var(--brown-color);
    border: 2px solid var(--brown-color);
    border-radius: 8px;
}

/*Cream text and arrow inside the brown dropdowns*/
div[class*="st-key-question_card"] div[data-baseweb="select"] * {
    color: var(--cream-color);
}

/*Buttons across the site (replaces the old gold button style)*/
.stButton button,
.stFormSubmitButton button,
.stDownloadButton button,
.stLinkButton a {
    background-color: var(--accent-color-neon-green);
    color: var(--navbar-color);
    font-weight: bold;
    border: none;
    border-radius: 12px;
    padding: 12px 20px;
    min-height: 48px;
}

.stButton button:hover,
.stFormSubmitButton button:hover,
.stDownloadButton button:hover,
.stLinkButton a:hover {
    background-color: var(--navbar-color);
    color: var(--accent-color-neon-green);
}
