import React, { useState } from 'react';

const HomePage = () => {
    const [username, setUsername] = useState('');
    const [githubUrl, setGithubUrl] = useState('');
    const [accessToken, setAccessToken] = useState('');
    const [isValid, setIsValid] = useState(false);

    const validateFields = () => {
        if (username && githubUrl && accessToken) {
            setIsValid(true);
        } else {
            setIsValid(false);
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (isValid) {
            // Handle form submission
        }
    };

    return (
        <div>
            <h1>PR generator</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => {
                        setUsername(e.target.value);
                        validateFields();
                    }}
                />
                <input
                    type="text"
                    placeholder="GitHub URL"
                    value={githubUrl}
                    onChange={(e) => {
                        setGithubUrl(e.target.value);
                        validateFields();
                    }}
                />
                <input
                    type="text"
                    placeholder="GitHub Access Token"
                    value={accessToken}
                    onChange={(e) => {
                        setAccessToken(e.target.value);
                        validateFields();
                    }}
                />
                <button type="submit" disabled={!isValid}>Submit</button>
            </form>
        </div>
    );
};

export default HomePage;