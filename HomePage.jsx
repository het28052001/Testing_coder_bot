import React, { useState } from 'react';

const HomePage = () => {
    const [githubUrl, setGithubUrl] = useState('');
    const [username, setUsername] = useState('');
    const [accessToken, setAccessToken] = useState('');

    const handleConfigure = () => {
        // Handle the configuration logic here
    };

    return (
        <div>
            <h1>Configuration Page</h1>
            <div>
                <label>
                    Github URL:
                    <input
                        type="text"
                        value={githubUrl}
                        onChange={(e) => setGithubUrl(e.target.value)}
                    />
                </label>
            </div>
            <div>
                <label>
                    Username:
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </label>
            </div>
            <div>
                <label>
                    Access Token:
                    <input
                        type="password"
                        value={accessToken}
                        onChange={(e) => setAccessToken(e.target.value)}
                    />
                </label>
            </div>
            <button onClick={handleConfigure}>Configure</button>
        </div>
    );
};

export default HomePage;