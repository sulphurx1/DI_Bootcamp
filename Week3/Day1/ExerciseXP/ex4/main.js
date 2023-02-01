const allBooks = [];

const firstBook = {
    title: 'Final Offer',
    author: 'Lauren Asher',
    image: 'https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B300%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&product=path%5B/pimages/9781728272221_p0_v4%5D&call=url%5Bfile:common/decodeProduct.chain%5D',
    alreadyRead: true
}

const secondBook = {
    title: 'Chain of Thorns',
    author: 'Cassandra Clare',
    image: 'https://prodimage.images-bn.com/lf?set=key%5Bresolve.pixelRatio%5D,value%5B1%5D&set=key%5Bresolve.width%5D,value%5B600%5D&set=key%5Bresolve.height%5D,value%5B10000%5D&set=key%5Bresolve.imageFit%5D,value%5Bcontainerwidth%5D&set=key%5Bresolve.allowImageUpscaling%5D,value%5B0%5D&set=key%5Bresolve.format%5D,value%5Bwebp%5D&source=url%5Bhttps://prodimage.images-bn.com/pimages/9781481431934_p0_v2_s600x595.jpg%5D&scale=options%5Blimit%5D,size%5B600x10000%5D&sink=format%5Bwebp%5D',
    alreadyRead: false
}

const listBook = document.getElementsByClassName('listBooks')[0];
const table = document.createElement('table')

listBook.appendChild(table);

table.innerHTML = `
    <tr>
        <th colspan = "3">List of Books</th>
    </tr>
    <tr class = "${firstBook.alreadyRead ? 'is-read' : ''}">
        <td>${firstBook.title} written by ${firstBook.author}</td>
        <td>
            <img src="${firstBook.image}" />
        </td>
        <td>Read status: ${firstBook.alreadyRead}</td>
    </tr>
    <tr class = "${secondBook.alreadyRead ? 'is-read' : ''}">
    <td>${secondBook.title} written by ${secondBook.author}</td>
    <td>
        <img src="${secondBook.image}" />
    </td>
    <td>Read status: ${secondBook.alreadyRead}</td>
</tr>
`
table.setAttribute("border", "2");


// loop to check for reading to fix in future
///////////////////////////////////////////////////////////////////////
// for(let i = 0, row; row = table.rows[i]; i++) {
//     for(let j = 0, col; col = row.cells[j]; j++) {
//         if(col === 'true'){
//             table.style.color = 'blue';
//         }
//     }
// }
// if(allBooks.alreadyRead === 'true') {
    
// }
///////////////////////////////////////////////////////////////////////

// function to generate table
///////////////////////////////////////////////////////////////////////
// generatedTable()
// function generateTable() {
//     const tbl = document.createElement('table');
    
//     // creating cells
//     for(let i = 0; i < 2; i++) {
//         const row = document.createElement('tr');
//     }

//     for(let j = 0; j < 2; j++) {
//         const cell = document.createElement('td');

//         row.appendChild(cell);
//     }
///////////////////////////////////////////////////////////////////////