// <!-- JavaScript for Mobile Menu Toggle -->
const menuBtn = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');
menuBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});


function showPopup(message, type) {
    const popup = document.getElementById('popup');
    const popupMessage = document.getElementById('popup-message');

    popupMessage.textContent = message;
    popup.className = `fixed top-5 right-5 px-4 py-3 rounded-lg shadow-md text-white bg-${type}-500`;

    popup.classList.remove('hidden');

    // Hide popup after 5 seconds
    setTimeout(() => {
        popup.classList.add('hidden');
    }, 3000);
}


document.querySelectorAll('pre').forEach((pre) => {
    // Create a copy button
    const button = document.createElement('button');
    button.innerHTML = '<i class="ri-file-copy-line"></i>';
    button.style.position = 'absolute';
    button.style.top = '10px';
    button.style.right = '10px';
    button.style.background = 'transparent';
    button.style.border = 'none';
    button.style.cursor = 'pointer';
    button.style.fontSize = '16px';

    // Ensure pre is a relatively positioned container
    pre.style.position = 'relative';

    // Append the button inside the pre block
    pre.appendChild(button);

    // Add click event to copy code
    button.addEventListener('click', () => {
        const code = pre.querySelector('code').textContent;
        navigator.clipboard.writeText(code).then(() => {
            button.textContent = 'Copied!';
            setTimeout(() => {
                button.innerHTML = '<i class="ri-file-copy-line"></i>';
            }, 2000);
        }).catch((err) => {
            console.error('Failed to copy code:', err);
        });
    });
});
