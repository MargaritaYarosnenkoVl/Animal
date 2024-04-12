document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.ended-page_show').forEach(function (showBlock) {
        showBlock.addEventListener('click', function () {
            var description = this.parentNode.querySelector('.ended-page_show_description');
            description.classList.toggle('active');

            var rotateButton = this.querySelector('.ended-page_rotate_button img');
            rotateButton.classList.toggle('rotated');
        });
    });
});