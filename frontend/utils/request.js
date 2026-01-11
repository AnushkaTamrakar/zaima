// 网络请求封装

// API基础URL
const baseURL = 'http://localhost:8000/api';

// 创建请求函数
const request = (url, method = 'GET', data = {}) => {
  // 获取token
  const token = uni.getStorageSync('token');
  
  // 构建请求头
  const header = {
    'Content-Type': 'application/json',
  };
  
  // 如果有token，添加到请求头
  if (token) {
    header['Authorization'] = `Bearer ${token}`;
  }
  
  // 返回Promise对象
  return new Promise((resolve, reject) => {
    uni.request({
      url: baseURL + url,
      method,
      data,
      header,
      success: (res) => {
        // 请求成功处理
        if (res.statusCode === 200) {
          resolve(res.data);
        } else if (res.statusCode === 401) {
          // 未授权，清除token，重新登录
          uni.removeStorageSync('token');
          // 可以在这里跳转到登录页面或重新获取token
          reject(new Error('未授权，请重新登录'));
        } else {
          // 其他错误
          reject(new Error(res.data.detail || '请求失败'));
        }
      },
      fail: (err) => {
        // 请求失败处理
        reject(err);
      },
      complete: () => {
        // 请求完成处理
      }
    });
  });
};

// 封装GET请求
request.get = (url, data = {}) => {
  return request(url, 'GET', data);
};

// 封装POST请求
request.post = (url, data = {}) => {
  return request(url, 'POST', data);
};

// 封装PUT请求
request.put = (url, data = {}) => {
  return request(url, 'PUT', data);
};

// 封装DELETE请求
request.delete = (url, data = {}) => {
  return request(url, 'DELETE', data);
};

// 封装PATCH请求
request.patch = (url, data = {}) => {
  return request(url, 'PATCH', data);
};

export default request;