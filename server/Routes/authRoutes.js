const { register, login } = require("../Controllers/authControllers");
const { checkUser } = require("../Middleware/authMiddleware");

const router = require("express").Router();

router.post("/", checkUser);
router.post("/register", register);
router.post("/login", login);

module.exports = router;