<template>
  <div class="about-container">
    <div class="header">
      <div class="app-logo">👻</div>
      <h1 class="app-name">zaima</h1>
      <p class="app-version">版本 1.0.0</p>
    </div>
    
    <div class="content">
      <div class="section">
        <h2 class="section-title">关于应用</h2>
        <p class="section-content">
          为独居人群打造的轻量化安全工具，通过签到监测与紧急联络机制，构建无感化安全防护，让独处生活更安心。
        </p>
      </div>
      
      <div class="section">
        <h2 class="section-title">核心功能</h2>
        <ul class="feature-list">
          <li class="feature-item">
            <span class="feature-icon">✅</span>
            <span class="feature-text">异常未签到自动通知</span>
          </li>
          <li class="feature-item">
            <span class="feature-icon">✅</span>
            <span class="feature-text">即开即用无负担</span>
          </li>
          <li class="feature-item">
            <span class="feature-icon">✅</span>
            <span class="feature-text">严格守护隐私安全</span>
          </li>
          <li class="feature-item">
            <span class="feature-icon">✅</span>
            <span class="feature-text">适合所有独居人群</span>
          </li>
        </ul>
      </div>
      
      <div class="section">
        <h2 class="section-title">隐私政策</h2>
        <p class="section-content">
          我们采用加密技术保护您的紧急联系人信息与签到记录，拒绝收集位置等无关权限，从源头杜绝隐私泄露风险，确保个人信息安全无忧。
        </p>
      </div>
      
      <div class="section">
        <h2 class="section-title">联系我们</h2>
        <p class="section-content">
          如有任何问题或建议，欢迎通过邮件与我们联系：
        </p>
        <p class="contact-email">support@zaima.com</p>
      </div>
    </div>
    
    <div class="footer">
      <p class="copyright">© 2026 zaima. 保留所有权利。</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // 页面数据
    };
  }
};
</script>

<style scoped>
.about-container {
  padding: 20px;
  background-color: #f8f8f8;
  min-height: calc(100vh - 50px);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.header {
  text-align: center;
  margin-bottom: 40px;
  padding-top: 20px;
}

.app-logo {
  font-size: 80px;
  margin-bottom: 15px;
}

.app-name {
  font-size: 32px;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
}

.app-version {
  font-size: 16px;
  color: #666;
}

.content {
  width: 100%;
  max-width: 600px;
}

.section {
  background-color: #ffffff;
  padding: 25px;
  border-radius: 12px;
  margin-bottom: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.section-title {
  font-size: 20px;
  font-weight: bold;
  color: #333;
  margin-bottom: 15px;
}

.section-content {
  font-size: 16px;
  color: #666;
  line-height: 1.6;
  margin-bottom: 15px;
}

.feature-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.feature-item {
  display: flex;
  align-items: center;
  margin-bottom: 12px;
  font-size: 16px;
  color: #666;
}

.feature-icon {
  margin-right: 10px;
  font-size: 18px;
  color: #4CD964;
}

.contact-email {
  font-size: 16px;
  color: #4CD964;
  font-weight: bold;
  text-align: center;
  margin-top: 10px;
}

.footer {
  margin-top: 40px;
  padding: 20px;
  text-align: center;
}

.copyright {
  font-size: 14px;
  color: #999;
}
</style>