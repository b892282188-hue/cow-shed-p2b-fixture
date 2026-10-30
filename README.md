# cow-shed-p2b-fixture

牛棚计划 P2-B 首次云端施工闭环的专用测试仓库。

- 全部内容均为虚构示例代码与测试数据，不含任何真实项目代码或个人数据。
- 用途：验证「GitHub 工单 → 可信授权 → Codex 施工 → Draft PR → CI → Evidence Card」闭环。
- 本仓库的 Issue、PR 与提交均由实验流程产生，合并与否由仓库所有者手动决定，实验流程永不自动合并。

## 结构

- `mathutils.py`：极小的示例函数库。
- `tests/`：Python unittest 单元测试。
- `.github/workflows/test.yml`：GitHub Actions 测试工作流。

## 本地运行测试

```bash
python3 -m unittest discover -s tests -t . -v
```
