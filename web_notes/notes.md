# HTML 
- There are more than 50 billion web pages
- Web pages designed for viewing in browser
- Web pages are defined using HTML
- HTML documents are text files 
- Can also be accessed programmatically via Python and packages
- pandas can be used to access data in a table in a web page
- For non-tabular data, can use other packages, e.g., -requests package to access a web page -*Beautiful Soup package (bs4) to locate data of interest on the page
- Create this html file using your text editor
- ![image](https://github.com/user-attachments/assets/c6f765a0-df6f-45f4-a0e6-b55940086fd2)
- There can multple levels of headers `<h1>, <h2>, <h3>, <h4>, <h5>, <h6>`
- The number indicates the relative size; `<h1>` is largest
- An HTML page can have different parts
- a division (part) of the page is denoted by the <div> tag
- a <span> usually identifies a smaller section, e.g., a phrase or data field
- HTML can be represented as a tree
- Tree elements have relationships: parent, child, sibling
- ![image](https://github.com/user-attachments/assets/3fa35590-5ac5-46cd-8221-3f2a78d03371)
- ![image](https://github.com/user-attachments/assets/cb812654-4548-4e0c-a83f-47efea3e13d4)
## HTML attributes
- An HTML attribute adds information to a tag
- An attribute has a name and a value
- Example attribute of id with value of 'asofdatetime'
- <div id='asofdatetime'> The id attribute is special, it can be used to uniquely identify tags
## HTML tables
- Since HTML has a tree structure, a table is represented as a tree
- html table is popular tag to display structured data
- Some table-related tags are:
- `<table>`
- `<tr>` - a row of the table
- `<td>` a data item in the table
- View the file using your browser
- ![image](https://github.com/user-attachments/assets/d46595ab-5233-4661-963a-ce6895e31b9d)
- Structure of a table
- ![image](https://github.com/user-attachments/assets/139a62c5-4043-457e-96c7-f66bd37503a4)
## Reading html file using Python
- To read html file and parse the page's tree structure
- Use the Beautiful Soup package (bs4)
- it provides methods to access any data on the page's tree
- - https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
## displaying the tree
- The find() method will return the first found tag of requested type(s)
- The find_all() method will return all found tags of requested type
- Other find methods allow navigating the HTML tree:
- Use requests package to access a document on the Web
## Beatiful Soup Methods for navigatint the tree
 - find('span')
 - 
  



