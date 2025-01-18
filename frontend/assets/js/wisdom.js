// 加载章节数据
fetch('http://127.0.0.1:8000/api/chapters/')
  .then(response => response.json())
  .then(data => {
    const sidebar = document.querySelector('.sidebar ul');
    const content = document.querySelector('.content');

    sidebar.innerHTML = ''; // 清空导航
    content.innerHTML = ''; // 清空内容

    data.forEach(chapter => {
      // 添加导航中的一级标题
      const listItem = document.createElement('li');
      listItem.textContent = chapter.title;
      listItem.onclick = () => scrollToSection(`section${chapter.id}`);
      sidebar.appendChild(listItem);

      // 添加内容中的一级标题
      const section = document.createElement('section');
      section.id = `section${chapter.id}`;
      section.innerHTML = `<h1>${chapter.title}</h1>${marked(chapter.content)}`;
      content.appendChild(section);

      // 添加内容中的二级标题
      chapter.sub_chapters.forEach(subChapter => {
        const subSection = document.createElement('div');
        subSection.innerHTML = `<h2>${subChapter.title}</h2>${marked(subChapter.content)}`;
        content.appendChild(subSection);
      });
    });
  })
  .catch(error => console.error('Error fetching chapters:', error));

// 滚动至特定章节
function scrollToSection(sectionId) {
  const section = document.getElementById(sectionId);
  if (section) {
    section.scrollIntoView({ behavior: 'smooth' });
  }
}
