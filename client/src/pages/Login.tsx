import PasswordToggleIcon from '../components/PasswordToggleIcon';
import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import api from '../api/axios';

function Register() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()

    try {
      setError('')

      const response = await api.post('/auth/login', {
        email,
        password,
      });
      console.log('Successful login', response.data);
      navigate('/dashboard')
    } catch (err: any) {
      if (err.response) {
        setError(err.response.data.msg || err.response.data.detail[0].ctx.reason || 'Something went wrong');
      } else {
        setError('Network Error');
      }
    }
  };



  const togglePassword = () => {
    setShowPassword((prev) => !prev)
  };


  return (
    <div className="min-h-screen flex items-center justify-center bg-pbblack px-2.5">
      <form onSubmit={handleSubmit} className="animate-slide-up-fade  text-left flex flex-col w-full h-full max-h-[316] max-w-[366px]">
        <div>
          <h1 className="text-pbwhite font-bold text-2xl mb-0.5">Log in to PromptBox</h1>
          <p className="mb-[30px] text-pbwhite text-base">Don't have an account? <Link to="/register" className="pb-link">Create one</Link></p>
        </div>
        <div className="flex flex-col">
          <label htmlFor="email" className="mb-2.5 text-pbwhite text-sm">
            Email
          </label>
          <input value={email} onChange={(e) => setEmail(e.target.value)} className="place-holder mb-5" id="email" type="text" placeholder="pixis@magic.com" />
        </div>
        <div className="flex flex-col">
          <label htmlFor="password" className="mb-2.5 text-pbwhite text-sm">
            Password
          </label>
          <div className="relative">
            <input value={password} onChange={(e) => setPassword(e.target.value)} className="w-full place-holder mb-7" id="password" type={showPassword ? "text" : "password"} placeholder="••••••••••" />
            <button  className="absolute right-4 top-[19px] cursor-pointer -translate-y-1/2 hover:opacity-85 transition" onClick={togglePassword} type="button">
              <PasswordToggleIcon visible={showPassword}></PasswordToggleIcon>
            </button>
          </div>
        </div>

        {error && (
          <div className='text-red-500 mb-4'>{error}</div>
        )}

        <button type="submit" className="white-button w-full">
          Continue
        </button>
      </form>
    </div>
  );
}

export default Register;
