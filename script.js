const ACCESS_TOKEN = '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'; // ใส่ GitHub Token ของ
const REPO_OWNER = 'Niceppn'; // ชื่อผู้ใช้ GitHub ของคุณ
const REPO_NAME = 'juniorYearr'; // ชื่อ repository ของคุณ
const BRANCH = 'Keep'; // ชื่อ branch ที่ต้องการอัปโหลดไฟล์
const FOLDER_PATH = 'assignment'; // โฟลเดอร์ที่ต้องการจัดเก็บไฟล์ใน repository

async function uploadFiles() {
    const fileInput = document.getElementById('fileInput');
    const files = fileInput.files;
    const fileTable = document.getElementById('fileTable').getElementsByTagName('tbody')[0];

    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        const row = fileTable.insertRow(-1);
        
        const nameCell = row.insertCell(0);
        const sizeCell = row.insertCell(1);
        const typeCell = row.insertCell(2);
        const statusCell = row.insertCell(3);
        const uploaderCell = row.insertCell(4);
        const downloadCell = row.insertCell(5);
        
        nameCell.textContent = file.name;
        sizeCell.textContent = formatFileSize(file.size);
        typeCell.textContent = file.type || 'Folder';
        statusCell.textContent = 'Uploading...';
        uploaderCell.textContent = localStorage.getItem('username') || 'Unknown';
        downloadCell.innerHTML = '<a href="#" onclick="downloadFile(\'' + file.name + '\')">Download</a>';

        await uploadToGitHub(file, statusCell);
    }
}

function formatFileSize(bytes) {
    if (bytes < 1024) return bytes + ' bytes';
    else if (bytes < 1048576) return (bytes / 1024).toFixed(2) + ' KB';
    else if (bytes < 1073741824) return (bytes / 1048576).toFixed(2) + ' MB';
    else return (bytes / 1073741824).toFixed(2) + ' GB';
}

async function uploadToGitHub(file, statusCell) {
    const base64Content = await fileToBase64(file);
    const path = `${FOLDER_PATH}/${file.name}`;
    const url = `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/contents/${path}`;

    const data = {
        message: `Upload ${file.name}`,
        content: base64Content,
        branch: BRANCH
    };

    try {
        const response = await fetch(url, {
            method: 'PUT',
            headers: {
                'Authorization': `token ${ACCESS_TOKEN}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            const errorDetails = await response.text();
            throw new Error(`Upload failed: ${response.status} ${response.statusText} - ${errorDetails}`);
        }

        const result = await response.json();
        console.log('File uploaded successfully:', result);
        statusCell.textContent = 'Upload successful';
        statusCell.style.color = 'green';
    } catch (error) {
        console.error('Error uploading file:', error);
        statusCell.textContent = 'Upload failed';
        statusCell.style.color = 'red';
    }
}

function fileToBase64(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onloadend = () => {
            const base64String = reader.result.replace('data:', '').replace(/^.+,/, '');
            resolve(base64String);
        };
        reader.onerror = reject;
        reader.readAsDataURL(file);
    });
}

function downloadFile(fileName) {
    // ฟังก์ชันนี้สามารถปรับแต่งเพิ่มเติมได้ตามที่ต้องการ สำหรับการดาวน์โหลดไฟล์จาก GitHub
}
