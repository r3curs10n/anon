-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 22, 2015 at 11:12 PM
-- Server version: 5.5.40-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `AI`
--

-- --------------------------------------------------------

--
-- Table structure for table `Answers`
--

CREATE TABLE IF NOT EXISTS `Answers` (
  `permalink` varchar(255) NOT NULL,
  `author` varchar(100) NOT NULL,
  `answer` text NOT NULL,
  `isRetrieved` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`permalink`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Answers`
--

INSERT INTO `Answers` (`permalink`, `author`, `answer`, `isRetrieved`) VALUES
('As-a-newbie-web-developer-should-I-use-a-framework-like-HTML5-Boilerplate-or-code-from-scratch/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('As-a-UX-designer-should-I-code-my-own-website-rather-than-using-Squarespace-for-jobs/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('Do-front-end-developers-use-Adobe-Creative-Suite-tools-Which-ones-are-useful/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('Front-End-Web-Development/What-is-the-most-bizarre-CSS-or-HTML-question-you-have-ever-been-asked-in-a-job-interview/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('Front-End-Web-Development/Which-tools-and-services-do-you-use-in-your-work/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('Happiness/What-was-were-your-best-moment-moments-in-2014/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('How-do-I-learn-to-code-1/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('How-do-I-start-learning-GitHub/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('How-does-it-feel-to-be-a-dualite-with-a-low-CGPA-in-BITS-Pilani-and-what-can-be-the-consequences-of-the-same/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('How-does-it-feel-to-be-a-GSoCer/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('How-is-that-none-of-the-IITs-have-been-able-to-replicate-the-practice-school-PS-II-model-that-BITS-Pilani-has-created-over-the-years/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('How-much-Python-must-I-know-to-be-able-to-prepare-for-SymPy-in-GSoC/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('How-should-a-freshman-in-computer-science-work-to-participate-in-GSoC-2015/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('I-am-single-child-with-working-parents-What-should-I-do-if-I-feel-very-alone-at-times/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('I-have-a-strength-based-phone-interview-at-Barclays-in-a-few-hours-What-can-I-still-do-now-to-improve-my-result/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('I-have-zero-graphic-design-skills-Can-I-still-make-a-good-UX-designer-interaction-designer/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('I-worked-on-Android-app-development-For-the-last-3-months-I-am-working-on-HTML5-CSS3-JavaScript-and-jQuery-to-develop-web-apps-and-cross-platform-mobile-web-apps-Is-there-any-scope-for-web-app-development-or-should-I-continue-to-Android-app-development/an', 'Raghu-Nayyar', '', 0),
('If-I-walk-up-to-a-Muslim-and-say-You-Muslims-are-thin-skinned-murderers-Islam-is-a-religion-of-violence-and-he-punches-me-in-the-face-will-my-words-be-considered-fighting-words/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('If-the-smartest-students-in-India-go-to-IIT-where-do-the-smartest-students-go-in-the-USA/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('Is-CoffeeScript-reliable/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('Is-it-worth-learning-jQuery/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('Is-there-anything-wrong-in-this-Please-let-me-know/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('Our-startup-is-planning-to-develop-a-cross-device-mobile-pc-tablet-web-application-we-are-use-to-the-regular-html-css-php-javascript-Workflow-is-there-any-other-workflow-to-be-used-other-than-these/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('Our-startup-is-planning-to-develop-a-cross-device-mobile-pc-tablet-web-application-We-are-used-to-the-regular-HTML-CSS-PHP-JavaScript-Workflow-Is-there-any-other-workflow-to-be-used-other-than-these/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('Smart-People/As-a-technical-person-what-is-your-reaction-when-you-hear-the-phrase-Its-not-what-you-know-Its-who-you-know/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('What-are-some-famous-scientists-who-didnt-graduate-from-a-top-ten-prestigious-college/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('What-are-some-good-pieces-of-music-to-listen-to-while-coding/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('What-are-some-interesting-GitHub-organizations/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('What-are-some-of-the-inconspicuous-non-digital-microinteractions-that-we-use-in-our-daily-live/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('What-are-some-organisations-that-a-beginner-contributor-should-choose-for-Google-Summer-of-Code/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('What-are-some-useful-coding-practices-that-dont-sound-that-useful-at-the-beginning/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('What-are-some-weird-things-that-turn-you-on/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('What-different-types-of-people-did-you-meet-in-2014/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('What-difficulties-are-faced-by-self-taught-programmers/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('What-does-it-feel-like-to-go-from-physically-unattractive-to-attractive/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('What-is-a-project-that-can-be-undertaken-by-a-first-year-second-year-electrical-electronics-and-instrumentation-undergraduate/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('What-major-website-has-the-best-design-right-now-Why/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('What-other-productive-things-can-be-done-on-Facebook-other-than-wasting-time/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('What-should-be-the-reply-to-the-question-why-did-you-not-do-any-projects/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('What-should-I-do-if-a-mean-girl-friend-texts-me-after-6-months/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('What-things-at-BITS-Goa-lowers-the-students-CGPA/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('What-would-be-a-sad-2-word-story/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('Which-is-the-best-GSOC-mentoring-organisation-for-those-who-know-only-C-and-C++/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('Which-line-gives-you-strength-when-everything-in-your-life-is-going-wrong/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0),
('Why-do-we-see-a-red-color-when-we-hold-our-palm-against-a-light-source/answer/Raghu-Nayyar', 'Raghu-Nayyar', '', 0);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
