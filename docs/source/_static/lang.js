// Get the URL of the current page
var currentURL = window.location.href;

// Check whether it is on the homepage
if (currentURL === "https://docs.sunfounder.com/projects/picar-x-v20/en/latest/") {
    // Get the user's browser language
    var userLang = navigator.language || navigator.userLanguage;

    // Cut the language code and keep only the first two characters (e.g. from "en-US" to "en")
    userLang = userLang.substr(0, 2);

    // Set different links based on the browser language settings
    var link;

    switch (userLang) {
        // case "de": // German 
        //     link = "https://docs.sunfounder.com/projects/picar-x-v20/de/latest/";
        //     break;
        // case "ja": // Japanese
        //     link = "https://docs.sunfounder.com/projects/picar-x-v20/ja/latest/";
        //     break;
        default: // Default (English)
            link = "https://docs.sunfounder.com/projects/picar-x-v20/en/latest/";
    }

    // Only execute the jump if the current page is not the target link to prevent repeated jumps
    if (currentURL !== link) {
        window.location.href = link;
    }
}