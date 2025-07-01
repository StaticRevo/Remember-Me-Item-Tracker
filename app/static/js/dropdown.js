document.querySelector('.dropdown').addEventListener('click', function (e) {
  e.stopPropagation();
  const menu = this.querySelector('.dropdown-menu');
  menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
});

document.addEventListener('click', function () {
  document.querySelectorAll('.dropdown-menu').forEach(menu => menu.style.display = 'none');
});
