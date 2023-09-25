import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import image from '../../assets/images/logo.jpg'

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
		<div className='navbar-container'>
			<ul className='navbar-content'>
				<li>
				<NavLink exact to="/" style={{color: 'white'}}><img src={image}></img></NavLink>
				</li>
				{isLoaded && (
					<li>
						<ProfileButton user={sessionUser} />
						<>This is the profile button</>
					</li>
				)}
			</ul>
		</div>

	);
}

export default Navigation;
