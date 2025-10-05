let currentCards = [];

function drawCards() {
    // 显示加载状态
    document.getElementById('loadingText').textContent = '正在为您抽取塔罗牌...';
    showLoading();
    
    // 发送抽牌请求
    fetch('/draw-cards', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            currentCards = data.cards;
            showCards(data.cards);
        } else {
            showError(data.error || '抽牌过程中出现错误');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showError('网络错误，请稍后重试');
    });
}

function generateReading() {
    const questionInput = document.getElementById('questionInput');
    const question = questionInput.value.trim();
    
    if (!question) {
        alert('请输入您的问题！');
        return;
    }
    
    if (!currentCards || currentCards.length === 0) {
        alert('请先抽取塔罗牌！');
        return;
    }
    
    // 显示加载状态
    document.getElementById('loadingText').textContent = '正在解读...';
    showLoading();
    
    // 发送解读请求
    fetch('/divination', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
            question: question,
            cards: currentCards
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showResult(data.reading);
        } else {
            showError(data.error || '解读过程中出现错误');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showError('网络错误，请稍后重试');
    });
}

function showLoading() {
    document.getElementById('drawSection').style.display = 'none';
    document.getElementById('cardsSection').style.display = 'none';
    document.getElementById('loadingSection').style.display = 'block';
    document.getElementById('resultSection').style.display = 'none';
}

function showCards(cards) {
    const cardsContainer = document.getElementById('cardsContainer');
    
    // 显示塔罗牌
    cardsContainer.innerHTML = '';
    cards.forEach((card, index) => {
        const cardElement = document.createElement('div');
        cardElement.className = 'card';
        cardElement.innerHTML = `
            <div class="card-color-block" style="background-color: ${card.color}">
                <div class="card-name">${card.name}</div>
            </div>
            <div class="card-position">${card.position}</div>
            <div class="card-meaning">${card.meaning}</div>
        `;
        cardsContainer.appendChild(cardElement);
    });
    
    // 显示牌面区域
    document.getElementById('loadingSection').style.display = 'none';
    document.getElementById('cardsSection').style.display = 'block';
}

function showResult(reading) {
    const readingContainer = document.getElementById('readingContainer');
    
    // 显示解读
    readingContainer.innerHTML = `
        <div class="reading-text">${reading}</div>
    `;
    
    // 显示结果区域
    document.getElementById('loadingSection').style.display = 'none';
    document.getElementById('cardsSection').style.display = 'none';
    document.getElementById('resultSection').style.display = 'block';
}

function showError(errorMessage) {
    const readingContainer = document.getElementById('readingContainer');
    readingContainer.innerHTML = `
        <div class="reading-text" style="color: #dc3545;">
            <strong>错误：</strong>${errorMessage}
        </div>
    `;
    
    document.getElementById('loadingSection').style.display = 'none';
    document.getElementById('resultSection').style.display = 'block';
}

function resetDivination() {
    document.getElementById('questionInput').value = '';
    currentCards = [];
    document.getElementById('drawSection').style.display = 'block';
    document.getElementById('cardsSection').style.display = 'none';
    document.getElementById('loadingSection').style.display = 'none';
    document.getElementById('resultSection').style.display = 'none';
}

// 页面加载完成后的初始化
document.addEventListener('DOMContentLoaded', function() {
    const questionInput = document.getElementById('questionInput');
    const divinationBtn = document.getElementById('divinationBtn');
    
    // 监听输入框变化
    questionInput.addEventListener('input', function() {
        divinationBtn.disabled = !this.value.trim();
    });
    
    // 监听回车键
    questionInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && e.ctrlKey) {
            startDivination();
        }
    });
    
    // 初始状态
    divinationBtn.disabled = true;
});
