import { axiosClient } from '../api/axiosClient';

export interface LoginPayload {
  username: string;
  password: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
  role: string;
  user_email: string;
  user_full_name: string;
}

export const authService = {
  async login(payload: LoginPayload): Promise<LoginResponse> {
    const response = await axiosClient.post<LoginResponse>('/auth/login', payload);
    return response.data;
  },
  
  async checkHealth(): Promise<{ status: string }> {
    const response = await axiosClient.get<{ status: string }>('/health');
    return response.data;
  }
};
