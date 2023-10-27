document.addEventListener("DOMContentLoaded", function() {
    var links = document.querySelectorAll('a[href^="https://docs.sunfounder.com/projects/ezblock3"]');
    links.forEach(function(link) {
        link.setAttribute('target', '_blank');
    });
});
