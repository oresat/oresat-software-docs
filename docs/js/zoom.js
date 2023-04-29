document.addEventListener('DOMContentLoaded', function() {
    var mermaidDivs = document.querySelectorAll('.mermaid');

    mermaidDivs.forEach(function(mermaidDiv) {
        mermaidDiv.style.overflow = 'scroll';
        mermaidDiv.style.transformOrigin = '0 0';
        mermaidDiv.style.transform = 'scale(1)';

        var zoomLevel = 1;

        mermaidDiv.addEventListener('wheel', function(event) {
            event.preventDefault();
            var deltaY = event.deltaY * -0.01;

            // Handle trackpad pinch-to-zoom gesture
            if (event.ctrlKey) {
                deltaY = deltaY * 5; // Increase zoom sensitivity for trackpad
            }

            zoomLevel += deltaY;
            zoomLevel = Math.min(Math.max(0.5, zoomLevel), 2); // Limit zoom level between 0.5 and 2
            mermaidDiv.style.transform = 'scale(' + zoomLevel + ')';
        });
    });
});
