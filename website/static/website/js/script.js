document.addEventListener("DOMContentLoaded", function () {

    /* =========================================
       MOBILE MENU
    ========================================= */

    const menuBtn = document.getElementById("menuBtn");
    const navLinks = document.getElementById("navLinks");

    if (menuBtn && navLinks) {

        menuBtn.addEventListener("click", function () {

            navLinks.classList.toggle("active");

        });


        const links = navLinks.querySelectorAll("a");

        links.forEach(function (link) {

            link.addEventListener("click", function () {

                navLinks.classList.remove("active");

            });

        });

    }


    /* =========================================
       PACKAGE → ENQUIRY FORM
    ========================================= */

    const packageButtons =
        document.querySelectorAll(".package-btn");

    const destinationInput =
        document.getElementById("id_destination");

    packageButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const packageName =
                button.getAttribute("data-package");

            if (
                destinationInput &&
                packageName
            ) {

                destinationInput.value = packageName;

            }

        });

    });


    /* =========================================
       SUCCESS MESSAGE
    ========================================= */

    const successMessage =
        document.querySelector(".success-message");

    if (successMessage) {

        setTimeout(function () {

            successMessage.style.opacity = "0";

            successMessage.style.transition =
                "opacity 0.5s ease";

            setTimeout(function () {

                successMessage.style.display = "none";

            }, 500);

        }, 5000);

    }

});