# Git Sync Checklist
**Last Updated:** $(date +%Y-%m-%d)

### Steps to Sync Changes
1. **Stage Changes**:
   ```sh
   git add .
   ```
2. **Commit**:
   ```sh
   git commit -m "Update: $(date +%Y-%m-%d)"
   ```
3. **Push**:
   ```sh
   git push
   ```
4. **Pull (if collaborating)**:
   ```sh
   git pull
   ```

### Notes
- Use `git status` to review changes before committing
- For merge conflicts, refer to [Git's documentation](https://git-scm.com/docs) 