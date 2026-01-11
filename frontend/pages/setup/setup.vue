<template>
  <div class="setup-container">
    <h1 class="page-title">紧急联系人设置</h1>
    
    <div class="form-container">
      <div class="form-group">
        <label for="name" class="form-label">联系人姓名</label>
        <input 
          type="text" 
          id="name" 
          v-model="contactForm.name" 
          class="form-input" 
          placeholder="请输入联系人姓名"
        >
      </div>
      
      <div class="form-group">
        <label for="email" class="form-label">联系人邮箱</label>
        <input 
          type="email" 
          id="email" 
          v-model="contactForm.email" 
          class="form-input" 
          placeholder="请输入联系人邮箱"
        >
      </div>
      
      <div class="form-note">
        <text>请确保邮箱地址正确，系统将在您连续多日未签到时发送邮件通知</text>
      </div>
      
      <button 
        class="save-button"
        :disabled="!contactForm.name || !contactForm.email"
        @click="saveContact"
      >
        保存
      </button>
    </div>
    
    <!-- 当前联系人信息 -->
    <div class="current-contact" v-if="currentContact">
      <h2 class="section-title">当前联系人</h2>
      <div class="contact-item">
        <text class="contact-label">姓名：</text>
        <text class="contact-value">{{ currentContact.name }}</text>
      </div>
      <div class="contact-item">
        <text class="contact-label">邮箱：</text>
        <text class="contact-value">{{ currentContact.email }}</text>
      </div>
    </div>
  </div>
</template>

<script>
import request from '../../utils/request';

export default {
  data() {
    return {
      contactForm: {
        name: '',
        email: ''
      },
      currentContact: null
    };
  },
  onLoad() {
    // 获取当前联系人信息
    this.getCurrentContact();
  },
  methods: {
    // 获取当前联系人
    async getCurrentContact() {
      try {
        const res = await request.get('/contact');
        this.currentContact = res;
        // 填充表单
        this.contactForm.name = res.name;
        this.contactForm.email = res.email;
      } catch (err) {
        console.error('获取联系人失败:', err);
        // 没有联系人时不报错
      }
    },
    
    // 保存联系人
    async saveContact() {
      try {
        // 验证表单
        if (!this.contactForm.name || !this.contactForm.email) {
          uni.showToast({
            title: '请填写完整信息',
            icon: 'none',
            duration: 2000
          });
          return;
        }
        
        // 保存联系人
        const res = await request.post('/contact', this.contactForm);
        
        // 更新当前联系人信息
        this.currentContact = res;
        
        // 显示成功提示
        uni.showToast({
          title: '保存成功',
          icon: 'success',
          duration: 2000
        });
      } catch (err) {
        console.error('保存联系人失败:', err);
        uni.showToast({
          title: '保存失败，请重试',
          icon: 'none',
          duration: 2000
        });
      }
    }
  }
};
</script>

<style scoped>
.setup-container {
  padding: 20px;
  background-color: #f8f8f8;
  min-height: calc(100vh - 50px);
}

.page-title {
  font-size: 24px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 30px;
  color: #333;
}

.form-container {
  background-color: #ffffff;
  padding: 25px;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 30px;
}

.form-group {
  margin-bottom: 20px;
}

.form-label {
  display: block;
  font-size: 16px;
  font-weight: bold;
  color: #333;
  margin-bottom: 8px;
}

.form-input {
  width: 100%;
  padding: 12px 15px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-sizing: border-box;
  transition: all 0.3s ease;
}

.form-input:focus {
  border-color: #4CD964;
  box-shadow: 0 0 0 2px rgba(76, 217, 100, 0.2);
}

.form-note {
  font-size: 14px;
  color: #666;
  margin-bottom: 20px;
  line-height: 1.5;
}

.save-button {
  width: 100%;
  padding: 15px;
  font-size: 18px;
  font-weight: bold;
  background-color: #4CD964;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.save-button:hover {
  background-color: #34C759;
}

.save-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.current-contact {
  background-color: #ffffff;
  padding: 25px;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.section-title {
  font-size: 20px;
  font-weight: bold;
  color: #333;
  margin-bottom: 20px;
}

.contact-item {
  margin-bottom: 15px;
  font-size: 16px;
}

.contact-label {
  color: #666;
  margin-right: 10px;
}

.contact-value {
  color: #333;
  font-weight: bold;
}
</style>