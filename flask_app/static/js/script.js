const toggleButton = document.getElementById('toggleButton');
const sidebar = document.getElementById('sidebar');
const mainContent = document.getElementById('mainContent');

toggleButton.addEventListener('click', () => {
  sidebar.classList.toggle('sidebar-hidden');
  mainContent.classList.toggle('main-content-full');
});