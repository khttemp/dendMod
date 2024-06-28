private void UpdateTrainOrg()
{
	this.RateCnt = 0;
	this.rate = this.MgrUpdate;
	if (this.mTrainOrg != null && this.TrainUpdate)
	{
		for (int i = 0; i < this.mTrainOrg.Length; i++)
		{
			if (this.mTrainOrg[i] != null)
			{
				this.mTrainOrg[i].FrameStart();
			}
		}
	}
	for (int j = 0; j < 9999; j++)
	{
		if (this.Option_FrameLoop)
		{
			if (this.rate > 0.0166f)
			{
				this.now_rate = 0.0166f;
			}
			else
			{
				this.now_rate = this.rate;
			}
		}
		this.MgrUpdate_FPS = this.now_rate * 60f;
		this.SetFramePer(this.now_rate / 0.0166f);
		if (this.mControll != null)
		{
			this.mControll.Update_Sync(this.now_rate);
		}
		if (this.mComicMgr != null)
		{
			this.mComicMgr.UpdateScript(this.now_rate);
		}
		if (this.mMsgWnd != null)
		{
			this.mMsgWnd.Sync(this.now_rate / this.GameSpeed());
		}
		if (this.IsBtlMode() && this.mMsgWnd2P != null)
		{
			this.mMsgWnd2P.Sync(this.now_rate / this.GameSpeed());
		}
		if (this.FVTMgr != null)
		{
			this.FVTMgr.UpdateFVT(this.now_rate / this.GameSpeed());
		}
		if (this.mTrainOrg != null && this.TrainUpdate)
		{
			for (int k = 0; k < this.mTrainOrg.Length; k++)
			{
				if (this.mTrainOrg[k] != null)
				{
					this.mTrainOrg[k].StartUpdate(this.now_rate);
					if (this.mTrainOrg[0].mBtlTrain.GetAdd() > 0f)
					{
						int railIndex = this.mTrainOrg[0].BodyList[0].m_Track[0].FrontWheel.NowRail.Parent.RailIndex;
						int boneNo = this.mTrainOrg[0].BodyList[0].m_Track[0].FrontWheel.NowRail.BoneNo;
						if (this.mTrainOrg[0].Dir == -1)
						{
							RailLine prevRailLine = SingletonMonoBehaviour<cGameMgr>.Instance.mRailMgr.GetRailLine(railIndex, boneNo).GetPrevRailLine();
							Debug.Log(string.Concat(new string[]
							{
								"railPos: (",
								railIndex.ToString(),
								", ",
								boneNo.ToString(),
								")\t",
								"[dir]:",
								this.mTrainOrg[0].BodyList[0].m_Track[0].FrontWheel.NowRail.transform.eulerAngles.ToString(),
								"\t",
								"prevRailPos: (",
								prevRailLine.Parent.RailIndex.ToString(),
								", ",
								prevRailLine.BoneNo.ToString(),
								")"
							}));
						}
						else
						{
							RailLine nextRailLine = SingletonMonoBehaviour<cGameMgr>.Instance.mRailMgr.GetRailLine(railIndex, boneNo).GetNextRailLine();
							Debug.Log(string.Concat(new string[]
							{
								"railPos: (",
								railIndex.ToString(),
								", ",
								boneNo.ToString(),
								")\t",
								"[dir]:",
								this.mTrainOrg[0].BodyList[0].m_Track[0].FrontWheel.NowRail.transform.eulerAngles.ToString(),
								"\t",
								"nextRailPos: (",
								nextRailLine.Parent.RailIndex.ToString(),
								", ",
								nextRailLine.BoneNo.ToString(),
								")"
							}));
						}
					}
					if (this.RateCnt == 0)
					{
						this.mTrainOrg[k].SpeedSave();
					}
				}
			}
		}
		if (!this.Option_FrameLoop)
		{
			break;
		}
		this.rate -= 0.0166f;
		if (this.rate <= 0f)
		{
			break;
		}
		this.RateCnt++;
	}
	this.MgrUpdate_FPS = this.MgrUpdate * 60f;
	this.SetFramePer(this.MgrUpdate / 0.0166f);
	if (this.mTrainOrg != null && this.TrainUpdate)
	{
		for (int l = 0; l < this.mTrainOrg.Length; l++)
		{
			if (this.mTrainOrg[l] != null)
			{
				this.mTrainOrg[l].BodyUpdate_NoSync(this.MgrUpdate);
			}
		}
	}
}