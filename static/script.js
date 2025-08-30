window.addEventListener('DOMContentLoaded', () => {
  const savedTheme = localStorage.getItem('theme');

  if (savedTheme === 'dark') {
    document.body.classList.add('dark-mode');
    // Optional: update icon if needed
    toggleIcon(true);
  }
});



function toggleDarkMode() {
  const body = document.body;
//   const themeIcon = document.getElementById('dm');

  body.classList.toggle('dark-mode');

   if (body.classList.contains('dark-mode')) {
    localStorage.setItem('theme', 'dark');
  } else {
    localStorage.setItem('theme', 'light');
    }
}


function setupThemeToggle() {
  const toggleBtn = document.getElementById('dm');

  if (!toggleBtn) {
    console.error('No element with id "theme-toggle" found!');
    return;
  }

  toggleBtn.addEventListener('click', toggleDarkMode);
}

// Call function when DOM is ready
document.addEventListener('DOMContentLoaded', setupThemeToggle);